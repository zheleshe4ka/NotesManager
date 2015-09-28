# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Notes(models.Model):
	class Meta():
		db_table = "notes"
	notes_title = models.CharField(max_length = 100)
	notes_text = models.TextField()
	notes_date = models.DateTimeField()
	notes_favorite = models.BooleanField()
	notes_category = models.CharField(max_length = 10)
