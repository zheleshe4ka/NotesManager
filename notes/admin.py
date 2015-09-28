from django.contrib import admin
from notes.models import Notes
# Register your models here.

class NotesAdmin(admin.ModelAdmin):
	fields = ['notes_title', 'notes_text', 'notes_date', 'notes_favorite', 'notes_category']
	list_filter = ['notes_date', 'notes_category', 'notes_favorite']

admin.site.register(Notes, NotesAdmin)