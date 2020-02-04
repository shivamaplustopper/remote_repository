from django.contrib import admin
from .models import *
# Register your models here.

class Banglore_admin(admin.ModelAdmin):
    list_display = ['company','position','experience','domain','skill','email_id']

class Hyderabad_admin(admin.ModelAdmin):
    list_display = ['company','position','experience','domain','skill','email_id']

class Pune_admin(admin.ModelAdmin):
    list_display = ['company','position','experience','domain','skill','email_id']

class Chennai_admin(admin.ModelAdmin):
    list_display = ['company','position','experience','domain','skill','email_id']

admin.site.register(Banglore_model,Banglore_admin)
admin.site.register(Hyderabad_model,Hyderabad_admin)
admin.site.register(Pune_model,Pune_admin)
admin.site.register(Chennai_model,Chennai_admin)