from django.shortcuts import render, HttpResponseRedirect
from events.models import Event, Child, Parent, GalleryImage, Announcement
from events.forms import GalleryImageForm
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required

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

	context_dict = {}

	try:
		event = Event.objects.get(slug=event_slug)

		gallery_images = GalleryImage.objects.filter(
			event=event)

		context_dict = {}

		context_dict['event'] = event
		context_dict['gallery_images'] = gallery_images

	except Event.DoesNotExist:
		pass

	return render(request, 'events/event.html', context_dict)


def add_event(request):

	user = request.user

	if request.method == 'POST':
		event_form = EventForm(request.POST, request.FILES)


# Add content views

@login_required
def add_galleryimage(request, pk):

    user = request.user
    parent = Parent.objects.get(user=user)
    event = Event.objects.get(pk=pk)

    if request.method == 'POST':
        galleryimage_form = GalleryImageForm(request.POST, request.FILES)

        if galleryimage_form.is_valid():

            galleryimage_form.save(parent=parent, event=event, commit=True)

            return HttpResponseRedirect("/events/event/{}".format(event.slug))

        else:
            print (galleryimage_form.errors)

    else:
        galleryimage_form = GalleryImageForm()

    return render(request, 'events/add_galleryimage.html',
        {'galleryimage_form': galleryimage_form})
