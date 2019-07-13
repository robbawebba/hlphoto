from django.db import models

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
