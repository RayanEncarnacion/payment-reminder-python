from django.contrib import admin
from django.apps import apps

app_models = apps.get_app_config('payment_reminder').get_models()

for model in app_models:
    class AdminPanelModel(admin.ModelAdmin):  
        list_display = [field.name for field in model._meta.fields] 
                   
    admin.site.register(model, AdminPanelModel)
