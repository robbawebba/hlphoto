from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from gallery.models import Photo
from gallery.forms import OrderPrintsForm

class PhotosList(generic.ListView):
    model = Photo


def OrderPrints(request, key):
    photo = get_object_or_404(Photo, pk=key)
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = OrderPrintsForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # TODO: How do I save the new Order and return the Order ID?
            # redirect to a new URL?
            new_order = form.save(commit=False)
            new_order.total_cost = photo.price
            form.save()
            return HttpResponseRedirect(reverse('photos'))

    # If this is a GET (or any other method) create the default form.
    else:
        form = OrderPrintsForm()

    context = {
        'form': form,
        'photo': photo,
        'shipping_cost': 0.00, # free shipping!
        'total_cost': photo.price,
    }

    return render(request, 'gallery/order_view.html', context)
