import uuid
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

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


class Recipe(models.Model):
    """ Recipe model for the user all users can have many recipes and they are used to make orders. """
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=32)
    image = models.ImageField(null=True, blank=True, upload_to="images/recipes")
    ingredients = ArrayField(models.CharField(max_length=200), blank=True, null=True, default=list)
    #ingredients = models.CharField(max_length=10, blank=True, null=True)  # Needs to be a list or dictionary
    #tags = models.ManyToManyField('Tag', blank=True)
    prep_time = models.IntegerField(default=0)  # in minutes
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('-created',)


class Order(models.Model):
    """ Order class to make orders from recipes """

    class Completed(models.TextChoices):
        yes = 'yes'
        no = 'no'
        in_progress = 'in_progress'
        canceled = 'canceled'

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    time = models.IntegerField()  # in minutes
    by_user = models.CharField(max_length=10)
    for_user = models.CharField(max_length=10)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.CharField(max_length=11, choices=Completed.choices, default=Completed.in_progress)

    class Meta:
        ordering = ('-created',)


# class HistoryLog(models.Model):
#     """ History log class that logs the whole activity of a user """
#
#     class Completed(models.TextChoices):
#         yes = 'yes'
#         no = 'no'
#         in_progress = 'in_progress'
#
#     id = models.UUIDField(default=uuid.uuid4, primary_key=True)
#     by_user = models.CharField(max_length=10)
#     for_user = models.CharField(max_length=10)
#     recipe = models.ForeignKey(Recipe, null=True, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#     completed = models.CharField(max_length=11, choices=Completed.choices, default=Completed.in_progress)
#
#     class Meta:
#         ordering = ('-created',)


class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    owner = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
    review = models.TextField(max_length=300)
    by_user = models.CharField(max_length=10)
    for_user = models.CharField(max_length=10, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['by_user', 'owner']]
        ordering = ('-created',)


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=16)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('-created',)











