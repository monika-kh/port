from django.contrib import admin

# Register your models here.
from .models import Jobs, Apply

admin.site.register(Jobs)
admin.site.register(Apply)
