from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse
from address.models import AddressField
import uuid

# Photo represents a photo available for viewing and purchase in the Gallery
# * title: The name to display for a Photo
# * price: The cost of this photo for ordering
# * url  : The static URL where this photo is hosted
class Photo(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    url   = models.URLField(max_length=250)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('order-prints', args=[str(self.id)])

# Order represents a unique purchase order of prints of a specific photo.
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID associated with a customer's order")
    photo = models.ForeignKey('Photo', on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number can contain up to 15 digits and must follow the following format: '+999999999'")
    phone_number = models.CharField(validators=[phone_validator], max_length=17)
    address = AddressField(on_delete='models.CASCADE')

    PRINT_SIZES = [
        ('4x6', '4\"x6\"'),
        ('6x8', '6\"x8\"'),
        ('8x10','8\"x10\"'),
        ('10x12', '10\"x12\"'),
    ]

    print_size = models.CharField(
        max_length=5,
        choices=PRINT_SIZES,
        default='4x6',
    )

    shipping_cost = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    total_cost = models.DecimalField(max_digits=8, decimal_places=2)
