from django.contrib import admin
from .models import User, Page, Subscription, Cache

# Register your models here.
admin.site.register(User)
admin.site.register(Page)
admin.site.register(Subscription)
admin.site.register(Cache)
