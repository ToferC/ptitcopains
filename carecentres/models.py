from django.db import models
from django.utils.text import slugify
from pc_app.users.models import User

# 3rd party imports
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Models

class CareCentre(models.Model):
	name = models.CharField(max_length=128)
	tagline = models.CharField(max_length=256)
	owner = models.ForeignKey(User, related_name="creator")
	administrators = models.ManyToManyField(User, blank=True)
	
	# details
	english_description = models.TextField(max_length=2000)
	french_description = models.TextField(max_length=2000)
	image = models.ImageField(upload_to='carecentre_images/%Y/%m/%d/%H_%M_%S',
		default='carecentre/nothing.jpg')
	image_thumbnail = ImageSpecField(source='image',
		processors=[ResizeToFill(300, 200)],
		format='JPEG',
		options={'quality': 120})
	age_groups = models.CharField(max_length=255)
	rates = models.TextField(max_length=500)
	openings = models.BooleanField(default=True)
	features = models.TextField(max_length=500, blank=True, null=True)
	hours_of_operation = models.TextField(max_length=500)

	# location info
	street = models.CharField(max_length=255, blank=True, null=True)
	city = models.CharField(max_length=128, blank=True, null=True)
	province_or_state = models.CharField(max_length=128, blank=True, null=True)
	postal_code = models.CharField(max_length=7, blank=True, null=True)
	country = models.CharField(max_length=128, blank=True, null=True)
	latitude = models.FloatField(blank=True, null=True)
	longitude = models.FloatField(blank=True, null=True)
	zoom = models.IntegerField(blank=True, null=True)
	phone = models.CharField(max_length=12, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	slug = models.SlugField(unique=True, max_length=255)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(CareCentre, self).save(*args, **kwargs)

	def __str__(self):
		return self.name


class Event(models.Model):
	title = models.CharField(max_length=128)
	carecentre = models.ForeignKey(CareCentre)
	date = models.DateField('event date')
	theme = models.CharField(max_length=64)
	description = models.TextField(max_length=1000, blank=True)
	image = models.ImageField(upload_to='event_images/%Y/%m/%d/%H_%M_%S',
		default='event_images/nothing.jpg')
	image_thumbnail = ImageSpecField(source='image',
		processors=[ResizeToFill(300,200)],
		format='JPEG',
		options={'quality': 120})
	published = models.BooleanField(default=True)
	latitude = models.FloatField(blank=True, null=True)
	longitude = models.FloatField(blank=True, null=True)
	zoom = models.IntegerField(blank=True, null=True)
	slug = models.SlugField(unique=True, max_length=255)

	class Meta:
		ordering = ["date"]
		verbose_name_plural = "events"

	def save(self, *args, **kwargs):
		self.slug = slugify("{}-{}".format(self.title, self.date))
		super(Event, self).save(*args, **kwargs)

	def __str__(self):
		return self.title


class Parent(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	carecentre = models.ForeignKey(CareCentre)
	last_name = models.CharField(max_length=64)
	first_name = models.CharField(max_length=64)
	bio = models.TextField(max_length=500, blank=True)
	slug = models.SlugField(unique=True, max_length=255)

	def save(self, *args, **kwargs):
		self.slug = slugify("{}={}".format(self.last_name, self.first_name))
		super(Parent, self).save(*args, **kwargs)

	def __str__(self):
		return "{}-{}".format(self.last_name, self.first_name)


class Child(models.Model):
	last_name = models.CharField(max_length=64)
	first_name = models.CharField(max_length=64)
	carecentre = models.ForeignKey(CareCentre)
	allergies = models.TextField(max_length=1000, blank=True, null=True)
	birthday = models.DateField(blank=True, null=True)
	image = models.ImageField(upload_to='children_images/%Y/%m/%d/%H_%M_%S',
		default='children_images/smiley.jpg')
	image_thumbnail = ImageSpecField(source='image',
		processors=[ResizeToFill(300,200)],
		format='JPEG',
		options={'quality': 120})
	parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
	join_date = models.DateField()
	leave_date = models.DateField()
	slug = models.SlugField(unique=True, max_length=255)

	class Meta:
		ordering = ["birthday"]
		verbose_name_plural = "children"

	def save(self, *args, **kwargs):
		self.slug = slugify("{}-{}".format(self.last_name, self.first_name))
		super(Child, self).save(*args, **kwargs)

	def __str__(self):
		return "{}, {}".format(self.last_name, self.first_name)


class GalleryImage(models.Model):
	owner = models.ForeignKey(Parent)
	image = models.ImageField(upload_to='gallery_images/%Y/%m/%d/%H_%M_%S',
		default='gallery_images/nothing.jpg')
	image_thumbnail = ImageSpecField(source='image',
		processors=[ResizeToFill(300,200)],
		format='JPEG',
		options={'quality': 120})
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
	carecentre = models.ForeignKey(CareCentre)
	title = models.CharField(max_length=64)
	content = models.TextField(max_length=2000)
	date = models.DateTimeField(auto_now=True)
	published = models.BooleanField(default=True)

	class Meta:
		ordering = ["date"]

	def __str__(self):
		return self.title
