from django import forms
from .models import Restaurant, Item



class RestaurantForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = '__all__'
		#fields = ['name', 'description', 'opening_time', 'closing_time', 'logo'] 
		exclude = ['slug']



class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['name', 'description', 'restaurant', 'price', 'active']

		