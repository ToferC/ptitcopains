from django import forms
from django.forms import widgets
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import CheckboxSelectMultiple
from django.db.models import Q
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from events.models import Event, Announcement, Parent, Child, GalleryImage 

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineField

# Forms

class GalleryImageForm(forms.ModelForm): 
	"""Form for users to add images"""

	class Meta:
		model = GalleryImage
		fields = "__all__"
		exclude = ['owner', 'published_date', 'event']

	def __init__(self, *args, **kwargs):

		super(GalleryImageForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)
		self.helper.layout.append(
			FormActions(
				HTML("""<br><a committment="button" class="btn btn-default"
					ref="events/event/{{ event.slug }}">Cancel</a> """),
				Submit('save', 'Save'),))

	def save(self, parent, event, commit=False):
		instance = super(GalleryImageForm, self).save(commit=False)
		instance.owner=parent
		instance.event=event
		instance.save()
		return instance