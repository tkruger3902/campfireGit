"""Defines URL patterns for campfires."""

from django.urls import path

from . import views

app_name = 'campfires'
urlpatterns = [
	# Home Page
	path('', views.index, name='index'),

	# About Page
	path('about/', views.about, name='about'),

	# Show all story names
	path('names/', views.names, name='names'),

	# Page for a single story
	path('names/<int:name_id>/', views.name, name='name'),
]