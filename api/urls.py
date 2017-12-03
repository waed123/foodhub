from django.conf.urls import url
from .views import RestaurantListAPIView, RestaurantDetailAPIView, RestaurantDeleteAPIView, RestaurantCreateAPIView, RestaurantUpdateAPIView


urlpatterns = [
	url(r'^$', RestaurantListAPIView.as_view(), name="list"),
	url(r'^create/$', RestaurantCreateAPIView.as_view(), name="create"),
	url(r'^(?P<rest_slug>[-\w]+)/detail/$', RestaurantDetailAPIView.as_view(), name="detail"), 
	url(r'^(?P<rest_slug>[-\w]+)/delete/$', RestaurantDeleteAPIView.as_view(), name="delete"),
	url(r'^(?P<rest_slug>[-\w]+)/update/$', RestaurantUpdateAPIView.as_view(), name="update"),   
]