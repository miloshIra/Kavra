# Generated by Django 3.2.3 on 2022-11-09 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kavapp', '0003_alter_recipe_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(max_length=10, null=True),
        ),
    ]