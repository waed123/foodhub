from django.shortcuts import render, redirect
from . import models
from .forms import RestaurantForm, ItemForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.utils import timezone



def item_create(request):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404

	form = ItemForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect("restaurant_list")

	context = {
		"form":form,
	}
	return render(request, "item_create.html", context)





def item_update(request, item_slug):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	item = models.Item.objects.get(slug=item_slug)
	form = ItemForm(request.POST or None, instance = item)
	if form.is_valid():
		form.save()
		return redirect("restaurant_list")

	context = {
		"form":form,
		"item":item,
	}
	return render(request, "item_update.html", context)





def item_delete(request, item_slug):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	models.Item.objects.get(slug=item_slug).delete()
	return redirect("item_create")





def restaurant_list(request):
	objects = models.Restaurant.objects.all()

	query = request.GET.get("q")
	if query:
		objects = objects.filter(name__icontains=query)

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




def restaurant_detail(request, restaurant_slug):
	object = models.Restaurant.objects.get(slug=restaurant_slug)
	items = models.Item.objects.filter(restaurant=object) # restaurant.item_set.all()

	status = "open"
	if not request.user.is_staff:
		items = items.filter(active=True)

	if object.opening_time > timezone.now().time() or object.closing_time < timezone.now().time():
		status = "Closed"


	# if not (object.opening_time < timezone.now().time() and object.closing_time > timezone.now().time()):
	# 	status = "Closed"

	#item = object.item_set.all()
	context = {
		"object" : object,
		"status" : status,
		"items" : items,
		"time":timezone.now().time(),
	}
	return render(request, 'restaurant_detail.html', context)




def restaurant_create(request):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	form = RestaurantForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect("restaurant_list")
	context = {
		'form': form
	}
	return render(request, 'restaurant_create.html', context)



def restaurant_update(request, restaurant_slug):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	item = models.Restaurant.objects.get(slug=restaurant_slug)
	form = RestaurantForm(request.POST or None,request.FILES or None, instance = item)

	if form.is_valid():
		form.save()
		return redirect("restaurant_detail", restaurant_slug=restaurant_slug)
	context = {
		'form': form,
		"item": item,
	}
	return render (request, "restaurant_update.html", context)




def restaurant_delete(request, restaurant_slug):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	item = models.Restaurant.objects.get(slug=restaurant_slug)
	models.Item.objects.filter(restaurant=item.name).delete()
	item.delete()
	return redirect("restaurant_list")
