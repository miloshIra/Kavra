# Generated by Django 3.2.3 on 2022-11-09 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kavapp', '0006_alter_recipe_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
