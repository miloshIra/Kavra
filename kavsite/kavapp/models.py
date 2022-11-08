from django.db import models

# Create your models here.


class User(models.Model):
    """ Basic user model of the app """

    class Role(models.TextChoices):
        cook = 'cook'
        customer = 'customer'

    id = models.UUIDField(primary_key=True)
    role = models.CharField(max_length=8, choices=Role.choices, default=Role.customer)
    name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    username = models.CharField(max_length=16)
    email = models.EmailField(max_length=32)
    password = models.CharField(max_lenth=32)
    likes = models.IntegerField(default=0)
    orders_cooked = models.IntegerField(default=0)
    orders_bought = models.IntegerField(default=0)
    created = models.DateTimeField()


class Recipe(models.Model):
    """ Recipe model for the user all users can have many recipes and they are used to make orders. """
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=32)
    ingredients = models.Model()  # Needs to be a list or dictionary
    prep_time = models.IntegerField(max_length=4)  # in minutes
    user_id = models.CharField()  # this is the creator
    likes = models.IntegerField(default=0)
    created = models.DateTimeField()


class Order(models.Model):
    """ Order class to make orders from recipes """

    class Completed(models.TextChoices):
        yes = 'yes'
        no = 'no'
        in_progress = 'in_progress'

    id = models.UUIDField(primary_key=True)
    time = models.IntegerField()  # in minutes
    by_user_id = models.CharField()
    for_user_id = models.CharField()
    recipe_id = models.CharField()
    created = models.DateTimeField()
    completed = models.CharField(max_length=10, choices=Completed.choices, default=Completed.in_progress)


class HistoryLog(models.Model):
    """ History log class that logs the whole activity of a user """

    class Completed(models.TextChoices):
        yes = 'yes'
        no = 'no'
        in_progress = 'in_progress'

    id = models.UUIDField(primary_key=True)
    by_user_id = models.CharField()
    for_user_id = models.CharField()
    recipe_id = models.CharField()
    created = models.DateTimeField()
    completed = models.CharField(max_length=10, choices=Completed.choices, default=Completed.in_progress)


class Review(models.Model):
    id = models.UUIDField()
    review = models.TextField()
    by_user = models.CharField()
    for_user = models.CharField()
    text = models.TextField()
    created = models.DateTimeField()


class Tag(models.Model):
    id = models.UUIDField()
    name = models.CharField(max_length=12)
    recipe_id = models.CharField()











