from django.contrib import admin

# Register your models here.
from core.models import App, Service, ServiceTemplate, ServiceEnvironmentValue

admin.site.register(App)
admin.site.register(Service)
admin.site.register(ServiceTemplate)
admin.site.register(ServiceEnvironmentValue)