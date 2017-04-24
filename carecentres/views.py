from django.shortcuts import render, HttpResponseRedirect
from carecentres.models import Event, Child, Parent, GalleryImage, Announcement
from carecentres.forms import GalleryImageForm, CareCentre
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required

# Create your views here.

def index(request):
	# Base view for main event index

	context_dict = {}

	try:
		carecentres = CareCentre.objects.all()
		context_dict['carecentres'] = carecentres

	except CareCentre.DoesNotExist:
		carecentres = ['No Care Centres']

	return render(request, 'carecentres/index.html', context_dict)


def carecentre(request, carecentre_slug):

	context_dict = {}

	try:
		carecentre = CareCentre.objects.get(
			slug=carecentre_slug)
	except CareCentre.DoesNotExist:
		carecentre = ['None']

	announcements = Announcement.objects.filter(
		carecentre=carecentre)

	context_dict['carecentre'] = carecentre
	context_dict['announcements'] = announcements

	return render(request, 'carecentres/carecentre.html', 
		context_dict)


def events(request, carecentre_slug):

	context_dict = {}

	carecentre = CareCentre.objects.get(
		slug=carecentre_slug)

	try:
		events = Event.objects.filter(
		carecentre=carecentre)

	except Event.DoesNotExist:
		events = ['None']

	context_dict['carecentre'] = carecentre
	context_dict['events'] = events

	return render(request, 'carecentres/events.html', context_dict)


def event(request, carecentre_slug, event_slug):

	context_dict = {}

	carecentre = CareCentre.objects.get(slug=carecentre_slug)

	try:
		event = Event.objects.get(slug=event_slug)

		gallery_images = GalleryImage.objects.filter(
			event=event)

		context_dict = {}

		context_dict['carecentre'] = carecentre
		context_dict['event'] = event
		context_dict['gallery_images'] = gallery_images

	except Event.DoesNotExist:
		pass

	return render(request, 'carecentres/event.html', context_dict)


def add_event(request):

	user = request.user

	if request.method == 'POST':
		event_form = EventForm(request.POST, request.FILES)


# Add content views

@login_required
def add_galleryimage(request, carecentre_slug, pk):

    user = request.user
    parent = Parent.objects.get(user=user)
    event = Event.objects.get(pk=pk)
    carecentre = CareCentre.objects.get(
    	slug=carecentre_slug)

    context_dict = {}

    context_dict['event'] = event
    context_dict['carecentre'] = carecentre

    if request.method == 'POST':
        galleryimage_form = GalleryImageForm(request.POST, request.FILES)

        if galleryimage_form.is_valid():

            galleryimage_form.save(parent=parent, event=event, commit=True)

            return HttpResponseRedirect("/carecentres/{}/event/{}".format(
            	carecentre.slug, event.slug))

        else:
            print (galleryimage_form.errors)

    else:
        galleryimage_form = GalleryImageForm()

    return render(request, 'carecentres/add_galleryimage.html',
        {'galleryimage_form': galleryimage_form,
        'context_dict': context_dict})
