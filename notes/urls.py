from django.conf.urls import include, url


urlpatterns = [
    url(r'^notes/all/$', 'notes.views.notess'),
    url(r'^notes/get/(?P<notes_id>\d+)/$', 'notes.views.notes'),
    
    url(r'^', 'notes.views.notess'),

]
