from django.shortcuts import render, redirect
from . import models
from .forms import RestaurantForm



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

def restaurant_create(request):
	form = RestaurantForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect("restaurant_list")
	context = {
		'form': form
	}
	return render(request, 'restaurant_create.html', context)

def restaurant_update(request, restaurant_id):
	item = models.Restaurant.objects.get(id=restaurant_id)
	form = RestaurantForm(request.POST or None, instance = item)

	if form.is_valid():
		form.save()
		return redirect("restaurant_detail", rest_id=restaurant_id)
	context = {
		'form': form,
		"item": item,
	}
	return render (request, "restaurant_update.html", context)

def restaurant_delete(request, restaurant_id):
	item = models.Restaurant.objects.get(id=restaurant_id).delete()
	return redirect("restaurant_list")
