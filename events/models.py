from django.db import models
from django.utils.text import slugify
from pc_app.users.models import User

# Models


class Event(models.Model):
	title = models.CharField(max_length=128)
	date = models.DateField('event date')
	theme = models.CharField(max_length=64)
	description = models.TextField(max_length=1000, blank=True)
	image = models.ImageField(upload_to='event_images/%Y/%m/%d/%H_%M_%S',
		default='event_images/nothing.jpg')
	published = models.BooleanField(default=True)
	slug = models.SlugField(unique=True, max_length=255)

	class Meta:
		ordering = ["date"]
		verbose_name_plural = "events"

	def save(self, *args, **kwargs):
		self.slug = slugify(f"{self.title}-{self.date}")
		super(Event, self).save(*args, **kwargs)

	def __str__(self):
		return self.title


class Parent(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	last_name = models.CharField(max_length=64)
	first_name = models.CharField(max_length=64)
	bio = models.TextField(max_length=500, blank=True)
	slug = models.SlugField(unique=True, max_length=255)

	def save(self, *args, **kwargs):
		self.slug = slugify(f"{self.last_name}-{self.first_name}")
		super(Parent, self).save(*args, **kwargs)

	def __str__(self):
		return f"{self.last_name}, {self.first_name}"


class Child(models.Model):
	last_name = models.CharField(max_length=64)
	first_name = models.CharField(max_length=64)
	birthday = models.DateField(blank=True, null=True)
	image = models.ImageField(upload_to='children_images/%Y/%m/%d/%H_%M_%S',
		default='children_images/smiley.jpg')
	parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
	join_date = models.DateField()
	leave_date = models.DateField()
	slug = models.SlugField(unique=True, max_length=255)

	class Meta:
		ordering = ["birthday"]
		verbose_name_plural = "children"

	def save(self, *args, **kwargs):
		self.slug = slugify(f"{self.last_name}-{self.first_name}")
		super(Child, self).save(*args, **kwargs)

	def __str__(self):
		return f"{self.last_name}, {self.first_name}"


class GalleryImage(models.Model):
	owner = models.ForeignKey(Parent)
	image = models.ImageField(upload_to='gallery_images/%Y/%m/%d/%H_%M_%S',
		default='gallery_images/nothing.jpg')
	published_date = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=64, blank=True)
	event = models.ForeignKey(Event)
	published = models.BooleanField(default=True)

	class Meta:
		ordering = ["published_date"]

	def __str__(self):
		return self.title


class Announcement(models.Model):
	author = models.ForeignKey(User)
	title = models.CharField(max_length=64)
	content = models.TextField(max_length=2000)
	date = models.DateTimeField(auto_now=True)
	published = models.BooleanField(default=True)

	class Meta:
		ordering = ["date"]

	def __str__(self):
		return self.title
