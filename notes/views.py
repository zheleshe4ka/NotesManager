from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from notes.models import Notes
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf

# Create your views here.

def notess(request):
		return render_to_response('notess.html',{'notess': Notes.objects.all()
			,'username': auth.get_user(request).username
			})

def notes(request, notes_id = 1):
		return render_to_response('notes.html', {'notes': Notes.objects.get(id = notes_id)
			,'username': auth.get_user(request).username
			})