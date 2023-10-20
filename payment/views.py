
import os

import stripe
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from payment.models import Payment
from payment.serializer import PaymentSerializer
from payment.services import PaymentService, PaymentError


# from payment.services import StripePayment

class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['payment_method']#, 'paid_course', 'paid_lesson']
    ordering_fields = ['payment_date']


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def create(self, request, *args, **kwargs):
        payment_data = request.data
        payment_serializer = self.get_serializer(data=payment_data)

        print(payment_serializer.is_valid())
        print(payment_serializer.errors)

        if payment_serializer.is_valid():
            payment_serializer.save()

            stripe_handler = PaymentService()
            try:
                stripe_id = stripe_handler.create_payment(
                    user=request.user,
                    amount=payment_data.get('payment_amount'),
                    payment_method=payment_data.get('payment_method')
                ).id

                payment_instance = payment_serializer.instance
                payment_instance.stripe_id = stripe_id
                payment_instance.save()

                return Response({"stripe_id": stripe_id}, status=status.HTTP_201_CREATED)
            except PaymentError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PaymentRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            stripe.api_key = os.getenv('STRIPE_KEY')
            payment_intent = stripe.PaymentIntent.retrieve(pk)
            print(payment_intent)
            return Response(payment_intent, status=status.HTTP_200_OK)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)