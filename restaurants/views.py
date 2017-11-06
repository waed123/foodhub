from django.shortcuts import render
from . import models
# Create your views here.
def restaurant_list(request):
	context = {
		"objects": models.Restaurant.objects.all()
	}
	return render(request, 'restaurant_list.html', context)


def restaurant_detail(request, rest_id):
	context = {
		"object" : models.Restaurant.objects.get(id=rest_id)
	}
	return render(request, 'restaurant_detail.html', context)