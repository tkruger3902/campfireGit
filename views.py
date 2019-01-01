from django.shortcuts import render

def index(request):
	"""The home page for Campfire."""
	return render(request, 'campfires/index.html')

def about(request):
	"""The about page for Campfire."""
	return render(request, 'campfires/about.html')
