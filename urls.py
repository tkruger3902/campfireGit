"""Defines URL patterns for campfires."""

from django.urls import path

from . import views

app_name = 'campfires'
urlpatterns = [
	# Home Page
	path('', views.index, name='index'),

	# About Page
	path('about/', views.about, name='about'),
]