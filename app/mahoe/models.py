from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class Wallet(models.Model):
    moneyAmount = models.FloatField(default=200.00)

class PurchaseHistory(models.Model):
    purchase_price = models.FloatField()
    date = models.DateTimeField()
    amount = models.FloatField()
    spendedCash = models.FloatField()
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=25)
    wallet = models.ForeignKey(to=Wallet, on_delete=models.CASCADE)

class OwnedCoin(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=25)
    amount = models.FloatField()
    purchase_price = models.FloatField()
    wallet = models.ForeignKey(to=Wallet, on_delete=models.CASCADE)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    objects = UserManager()
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name='first name',
        max_length=255,
    )
    last_name = models.CharField(
        verbose_name='last address',
        max_length=255,
    )
    username = models.CharField(
        verbose_name='username',
        max_length=255,
        unique=True
    )
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [first_name, last_name, username]

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name