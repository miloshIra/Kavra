# Generated by Django 3.2.3 on 2022-11-09 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kavapp', '0007_alter_recipe_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='prep_time',
            field=models.IntegerField(default=0),
        ),
    ]