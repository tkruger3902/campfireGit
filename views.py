from django.shortcuts import render

from .models import Name

def index(request):
	"""The home page for Campfire."""
	return render(request, 'campfires/index.html')

def about(request):
	"""The about page for Campfire."""
	return render(request, 'campfires/about.html')

def names(request):
	"""Show all names of stories."""
	names = Name.objects.order_by('date_added')
	context = {'names': names}
	return render(request, 'campfires/names.html', context)
