# Generated by Django 4.2.5 on 2023-09-27 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_alter_payment_options_remove_payment_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'Cash'), ('transfer', 'Transfer')], max_length=150, verbose_name='payment_method'),
        ),
    ]
