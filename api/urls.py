from django.conf.urls import url
from .views import ItemDetailAPIView, RestaurantListAPIView, RestaurantDetailAPIView, RestaurantDeleteAPIView, RestaurantCreateAPIView, RestaurantUpdateAPIView


urlpatterns = [
	url(r'^$', RestaurantListAPIView.as_view(), name="list"),
	url(r'^create/$', RestaurantCreateAPIView.as_view(), name="create"),
	url(r'^(?P<slug>[-\w]+)/itemdetail/$', ItemDetailAPIView.as_view(), name="itemdetail"),
	url(r'^(?P<rest_slug>[-\w]+)/detail/$', RestaurantDetailAPIView.as_view(), name="detail"), 
	url(r'^(?P<rest_slug>[-\w]+)/delete/$', RestaurantDeleteAPIView.as_view(), name="delete"),
	url(r'^(?P<rest_slug>[-\w]+)/update/$', RestaurantUpdateAPIView.as_view(), name="update"),   
]