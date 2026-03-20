from django.db import models

# Create your models here.

class PaymentModel(models.Model):
    INCOME_EXPENSES_CHOICES = (
        ('income', 'income'),
        ('expenses', 'expenses')
    )

    date = models.DateField()
    summ = models.IntegerField()
    comment = models.TextField(blank=True)
    is_payed = models.BooleanField(default=False)
    income_expenses_type = models.CharField(max_length=8, choices=INCOME_EXPENSES_CHOICES, default='expenses')

class PaymentClassesModel(models.Model):
    payment = models.ForeignKey(PaymentModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)