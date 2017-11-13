from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=250)
	description = models.TextField()
	opening_time = models.TimeField()
	closing_time = models.TimeField()
	logo = models.ImageField(null=True, blank=True, upload_to="post_images")

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']