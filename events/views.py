from django.shortcuts import render
from events.models import Event, Child, Parent, GalleryImage, Announcement

# Create your views here.

def index(request):
	# Base view for main event index

	context_dict = {}

	try:
		events = Event.objects.all()
		context_dict['events'] = events

		announcement = Announcement.objects.latest(
			'date')
		context_dict['announcement'] = announcement

	except Event.DoesNotExist:
		events = ['No Events']

	return render(request, 'events/index.html', context_dict)


def event(request, event_slug):

	try:
		event = Event.objects.get(slug=event_slug)

		gallery_images = GalleryImage.objects.filter(
			event=event)

		context_dict = {}

		context_dict['event'] = event
		context_dict['gallery_images'] = gallery_images

	except EventDoesNotExist:
		pass

	return render(request, 'events/event.html', context_dict)


def add_event(request):

	user = request.user

	if request.method == 'POST':
		event_form = EventForm(request.POST, request.FILES)

