from django.shortcuts import render, HttpResponseRedirect
from carecentres.models import Event, Child, Parent, GalleryImage, Announcement
from carecentres.forms import GalleryImageForm, CareCentre, EventForm, CareCentreForm
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.template.defaultfilters import slugify

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


@login_required
def add_carecentre(request):

    user = request.user

    if request.method == 'POST':
        form = CareCentreForm(request.POST, request.FILES)

        if form.is_valid():

            carecentre_slug = slugify(form.cleaned_data['name'])

            form.save(owner=user, commit=True)

            return HttpResponseRedirect(
                "carecentres/carecentre/{}".format(carecentre_slug))

        else:
            print(form.errors)

    else:
        form = CareCentreForm()

    return render(request, 'carecentres/add_carecentre.html',
        {'form': form})


@login_required
def add_event(request, carecentre_slug):

    user = request.user
    parent = Parent.objects.get(user=user)
    carecentre = CareCentre.objects.get(
        slug=carecentre_slug)

    context_dict = {}

    context_dict['carecentre'] = carecentre

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)

        if form.is_valid():

            event_slug = slugify("{}-{}".format(
                form.cleaned_data['title'], form.cleaned_data['date']))

            form.save(parent=parent, carecentre=carecentre, commit=True)

            return HttpResponseRedirect("/carecentres/{}/event/{}".format(
                carecentre.slug, event_slug))

        else:
            print (form.errors)

    else:
        form = EventForm()

    return render(request, 'carecentres/add_event.html',
        {'form': form, 'carecentre': carecentre,
        'context_dict': context_dict})


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
