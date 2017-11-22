from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save




class Restaurant(models.Model):
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(blank=True)
	description = models.TextField()
	opening_time = models.TimeField()
	closing_time = models.TimeField()
	logo = models.ImageField(null=True, blank=True, upload_to="post_images")

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']


def create_slug(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug=new_slug
	exist = Restaurant.objects.filter(slug=slug).exists()
	if exist:
		new_slug="%s-%s"%(slug,Restaurant.objects.filter(slug=slug).first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_rest(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug=create_slug(instance)

pre_save.connect(pre_save_rest, sender=Restaurant)



class Item(models.Model):
	restaurant = models.ForeignKey(Restaurant)
	name=models.CharField(max_length=120)
	slug=models.SlugField(blank=True)
	description=models.TextField()
	price=models.DecimalField(max_digits=20, decimal_places=3)
	active=models.BooleanField(default=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering=['name']


def create_slug_item(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug=new_slug
	exist = Item.objects.filter(slug=slug).exists()
	if exist:
		new_slug="%s-%s"%(slug,Restaurant.objects.filter(slug=slug).first().id)
		return create_slug_item(instance, new_slug=new_slug)
	return slug

def pre_save_item(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug=create_slug_item(instance)

pre_save.connect(pre_save_item, sender=Item)







