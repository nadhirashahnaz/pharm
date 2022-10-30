from django.db import models
from django.conf import settings

# Create your models here.
class Pharmacy(models.Model):
	name = models.TextField(blank=True)
	address = models.TextField(blank=True)