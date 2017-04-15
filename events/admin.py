from django.contrib import admin
from events.models import Event, Parent, Child, GalleryImage, Announcement

# Register your models here.

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


admin.site.register(Event, EventAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(Parent, ParentAdmin)



