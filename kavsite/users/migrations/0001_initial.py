# Generated by Django 3.2.16 on 2022-11-16 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=24)),
                ('email', models.EmailField(blank=True, max_length=500, null=True)),
                ('first_name', models.CharField(blank=True, max_length=24)),
                ('last_name', models.CharField(blank=True, max_length=24)),
                ('role', models.CharField(choices=[('cook', 'Cook'), ('customer', 'Customer')], default='customer', max_length=8)),
                ('likes', models.IntegerField(default=0)),
                ('orders_cooked', models.IntegerField(default=0)),
                ('orders_bought', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
