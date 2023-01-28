from django.db import models

class Event(models.Model):
	text = models.CharField(max_length=100)
	image = models.ImageField(upload_to='event_images/')
	texts = models.CharField(max_length=100)
	