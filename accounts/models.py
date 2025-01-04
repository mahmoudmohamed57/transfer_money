import uuid
from django.db import models
from decimal import Decimal

class Account(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def transfer(self, target_account, amount):
        amount = Decimal(amount)
        if self.balance >= amount:
            self.balance -= amount
            target_account.balance += amount
            self.save()
            target_account.save()
            return True
        return False

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
