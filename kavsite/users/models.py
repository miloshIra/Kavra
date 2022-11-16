from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Django User models is connected to Profile model here it requires:
    # username
    # password
    # email
    # first_name
    # last_name


# class Profile(models.Model):
#     """ Basic user model of the app """
#
#     class Role(models.TextChoices):
#         cook = 'cook'
#         customer = 'customer'
#
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     role = models.CharField(max_length=8, choices=Role.choices, default=Role.customer)
#     likes = models.IntegerField(default=0)
#     orders_cooked = models.IntegerField(default=0)
#     orders_bought = models.IntegerField(default=0)
#     created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return str(self.user)
#
#     class Meta:
#         ordering = ('-created',)

# class Client(models.Model):
#     user = models.OneToOneField(User  )