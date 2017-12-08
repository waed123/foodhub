from django.shortcuts import render
from restaurants.models import Restaurant, Item
from rest_framework.generics import ListAPIView,RetrieveAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from .serializers import ItemDetailSerializer, RestaurantListSerializer, RestaurantDetailSerializer, RestaurantCreateUpdateSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.filters import SearchFilter


class ItemDetailAPIView(RetrieveAPIView):
	queryset = Item.objects.all() 
	serializer_class = ItemDetailSerializer
	lookup_field = 'slug'

	permission_classes = [IsAuthenticated]

class RestaurantListAPIView(ListAPIView):
	queryset = Restaurant.objects.all() 
	filter_backends = [SearchFilter]
	serializer_class = RestaurantListSerializer
	search_fields = ['name', 'description']

	permission_classes = [AllowAny]

class RestaurantDetailAPIView(RetrieveAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantDetailSerializer
	lookup_field = 'slug'
	lookup_url_kwarg = 'rest_slug'

	permission_classes = [IsAuthenticated]

class RestaurantDeleteAPIView(DestroyAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantListSerializer
	lookup_field = 'slug'    
	lookup_url_kwarg = 'rest_slug'

	permission_classes = [IsAuthenticated, IsAdminUser]


class RestaurantCreateAPIView(CreateAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantCreateUpdateSerializer

	permission_classes = [IsAuthenticated, IsAdminUser]
	

class RestaurantUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantCreateUpdateSerializer
	lookup_field = 'slug'    
	lookup_url_kwarg = 'rest_slug'

	permission_classes = [IsAuthenticated, IsAdminUser]


