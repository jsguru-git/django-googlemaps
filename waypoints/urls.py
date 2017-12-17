# Import django modules
from django.conf.urls import *
from waypoints.views import index

urlpatterns = [
	url(r'^$', index, name='waypoints-index'),
]