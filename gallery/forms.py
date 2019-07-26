from django.forms import ModelForm
from gallery.models import Order

class OrderPrintsForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['id', 'photo', 'total_cost', 'shipping_cost']
        
