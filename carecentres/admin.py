from django.contrib import admin
from carecentres.models import Event, Parent, Child, GalleryImage
from carecentres.models import Announcement, CareCentre

# Register your models here.

class CareCentreAdmin(admin.ModelAdmin):
	list_display = ('name', 'city')

class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'date', 'theme', 'published')

class ParentAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name')

class ChildAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'birthday')

class GalleryImageAdmin(admin.ModelAdmin):
	list_display = ('title', 'owner', 'published_date', 'published')

class AnnouncementAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'published')

admin.site.register(CareCentre, CareCentreAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(Parent, ParentAdmin)



