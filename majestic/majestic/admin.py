from django.contrib import admin

from .models import *


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'user_phone', 'user_email', 'date_sent', 'checked',)
    list_filter = ('date_sent', 'checked',)
    list_editable = ('checked',)
    fields = ['fullname', 'user_phone', 'user_email', 'message', 'checked',]