from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from waypoints.models import Waypoint

def index(request):
	'Display map'
	waypoints = Waypoint.objects.order_by('name')
	return render_to_response('waypoints/index.html', {
		'waypoints': waypoints,
		'content': render_to_string('waypoints/waypoints.html', {'waypoints': waypoints}),
	})
