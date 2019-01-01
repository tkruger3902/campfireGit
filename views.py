from django.shortcuts import render

def index(request):
	"""The home page for Campfire."""
	return render(request, 'campfires/index.html')
