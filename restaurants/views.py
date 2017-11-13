from django.shortcuts import render, redirect
from . import models
from .forms import RestaurantForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def restaurant_list(request):
	objects = models.Restaurant.objects.all()
	#paginations
	paginator = Paginator(objects, 2) # Show 25 contacts per page

	number = request.GET.get('page')

	try:
		objects = paginator.page(number)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		objects = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		objects = paginator.page(paginator.num_pages)

	context = {
		"objects": objects
	}
	return render(request, 'restaurant_list.html', context)


def restaurant_detail(request, rest_id):
	context = {
		"object" : models.Restaurant.objects.get(id=rest_id)
	}
	return render(request, 'restaurant_detail.html', context)

def restaurant_create(request):
	form = RestaurantForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect("restaurant_list")
	context = {
		'form': form
	}
	return render(request, 'restaurant_create.html', context)

def restaurant_update(request, restaurant_id):
	item = models.Restaurant.objects.get(id=restaurant_id)
	form = RestaurantForm(request.POST or None,request.FILES or None, instance = item)

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
