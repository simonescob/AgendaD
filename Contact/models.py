# Django Contact Models

from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
	# Models Structure
	
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	number = models.IntegerField()
	email = models.EmailField(blank=True, null=True)
	image = models.ImageField(upload_to="contact_photos/", blank=True, null=True)
	
	def __str__(self):
		# return firstname and lastname on the admin
		return "{} {}".format(self.first_name, self.last_name)