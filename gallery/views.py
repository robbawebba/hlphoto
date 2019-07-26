from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from gallery.models import Photo, Order
from gallery.forms import OrderPrintsForm

class PhotosList(generic.ListView):
    model = Photo


def OrderPrints(request, key):
    photo = get_object_or_404(Photo, pk=key)
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = OrderPrintsForm(request.POST)

        # Check if the form is valid, and complete data processing
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.total_cost = photo.price
            form.save()
            return HttpResponseRedirect(reverse('confirm', kwargs={'order_id':new_order.id}))

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

class OrderConfirmationView(generic.DetailView):
    model = Order
