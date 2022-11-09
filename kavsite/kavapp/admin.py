from django.contrib import admin
from .models import Recipe, Review, Tag, Order, HistoryLog, Profile
# Register your models here.


admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(Recipe)
admin.site.register(Order)
admin.site.register(Tag)
admin.site.register(HistoryLog)
