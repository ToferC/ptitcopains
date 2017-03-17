from django.contrib import admin
from events.models import Event, Parent, Child, GalleryImage, Announcement

# Register your models here.

admin.site.register(Event)
admin.site.register(Announcement)
admin.site.register(Child)
admin.site.register(GalleryImage)
admin.site.register(Parent)



