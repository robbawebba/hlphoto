from django.views import generic
from gallery.models import Photo

class PhotosList(generic.ListView):
    model = Photo
