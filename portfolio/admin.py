from django.contrib import admin
from .models import Portfolio, Project

# Register your models here.
admin.site.site_header = 'Quiz2'
admin.site.register(Portfolio)
admin.site.register(Project)