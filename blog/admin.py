from django.contrib import admin
from .models import *


class SubscriberAdmin(admin.ModelAdmin):
    #list_display = ["name", "email"]
    list_display = [field.name for field in Subscriber._meta.fields]
    list_filter = ['name',]
    search_fields = ['name', 'email']
    #exclude = ['email']
    #fields = ['email']
    #inlines =
    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)
