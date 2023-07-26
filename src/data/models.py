from django.conf import settings
from django.db import models


class TransactionCategory(models.Model):
    """
    Модель типа транзакции.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, name='Тип транзакции')
    description = models.CharField(max_length=255, null=True, name='Описание')
    positive = models.BooleanField(default=True, name='')


class TransactionTheme(models.Model):
    """
    Модель тематики транзакции.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, name='Тематика')
    description = models.CharField(max_length=255, null=True, name='Описание')
    theme_type = models.ForeignKey(TransactionCategory, on_delete=models.CASCADE, name='Т')


class Transaction(models.Model):
    """
    Модель транзакции.
    """

    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True, name='Дата')
    amount = models.DecimalField(max_digits=10, decimal_places=2, name='Сумма')
    transaction_type = models.CharField(max_length=255, null=True, name='Тип транзакции')
    description = models.CharField(max_length=255, null=True, name='Описание')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, name='Пользователь')
