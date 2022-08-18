from django.db import models

# Create your models here.


class Borrower(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=127, default='')


class Loan(models.Model):
    STATUS_CHOICES = [
        (0, 'new'),
        (1, 'active'),
        (2, 'closed'),
    ]

    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    borrower = models.ForeignKey(Borrower, models.CASCADE, related_name='loans')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
