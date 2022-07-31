from django.db import models
from django.contrib.auth.models import User


class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user}'s balance "


class Lender(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    conditions = models.TextField()
    Lender_approval = models.BooleanField(default=False)
    Borrower_approval = models.BooleanField(default=False)
    percentage = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)


    @property
    def total_all(self):
        total_all = self.amount * self.percentage/100
        total_all += self.amount
        return total_all

    def __str__(self):
        return f"{self.user} lending {self.amount} on {self.date_created}"


class Borrower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    conditions = models.TextField()
    percentage = models.IntegerField(default=0)
    Lender_approval = models.BooleanField(default=False)
    Borrower_approval = models.BooleanField(default=False)
    duration = models.IntegerField(default=0)

    @property
    def total(self):
        total = self.amount * self.percentage / 100
        total += self.amount
        return total

    def __str__(self):
        return f"{self.user }"