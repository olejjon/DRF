from django.urls import path

from payment.apps import PaymentConfig
from payment.views import PaymentListAPIView, PaymentCreateAPIView, PaymentRetrieveAPIView

app_name = PaymentConfig.name

urlpatterns = [
    path('', PaymentListAPIView.as_view(), name='payment'),
    path('create/', PaymentCreateAPIView.as_view(), name='payment'),
    path('<pk>/', PaymentRetrieveAPIView.as_view(), name='payment'),
]
