from django.contrib import admin
from . import models

# Register your models here.
class RestAdminModel(admin.ModelAdmin):
	class Meta:
		model = models.Restaurant

admin.site.register(models.Restaurant, RestAdminModel)