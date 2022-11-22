from django.contrib import admin
from .models import Recipe, Review, Order, Profile, Tag
# Register your models here.


admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(Recipe)
admin.site.register(Order)
admin.site.register(Tag)

