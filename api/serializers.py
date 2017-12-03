from rest_framework import serializers
from restaurants.models import Restaurant



class RestaurantListSerializer(serializers.ModelSerializer):
	detail_page = serializers.HyperlinkedIdentityField(
		view_name = "api:detail",
		lookup_field = "slug",
		lookup_url_kwarg = "rest_slug",
		)
	class Meta:
		model = Restaurant
		fields = ['name', 'logo', 'opening_time', 'closing_time', 'detail_page']

class RestaurantDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = ['id', 'name', 'slug', 'logo','description', 'opening_time', 'closing_time']

class RestaurantCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = ['name', 'logo', 'opening_time', 'closing_time']