from django.contrib import admin
from .models import Recipe, Review, Profile, Tag, Order, HistoryLog
# Register your models here.

admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(Recipe)
admin.site.register(Order)
admin.site.register(Tag)
admin.site.register(HistoryLog)