from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


# Django User models is connected to Profile model here it requires:
    # username
    # password
    # email
    # first_name
    # last_name


class Profile(models.Model):
    """ Basic user model of the app """

    class Role(models.TextChoices):
        cook = 'cook'
        customer = 'customer'

    # id = models.IntegerField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=24, blank=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    first_name = models.CharField(max_length=24, blank=True)
    last_name = models.CharField(max_length=24, blank=True)
    role = models.CharField(max_length=8, choices=Role.choices, default=Role.customer)
    likes = models.IntegerField(default=0)
    orders_cooked = models.IntegerField(default=0)
    orders_bought = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ('-created',)
