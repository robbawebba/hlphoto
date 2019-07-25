from django.core.management.base import BaseCommand, CommandError
from gallery.models import Photo

class Command(BaseCommand):
    help = 'Populate the database with the specified number of 400x400px photos from https://picsum.photos'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='The number of photos to generate. Count must be 1<=count<=1000.')

    def handle(self, *args, **options):
        count = options['count']
        if count < 1 or count > 1000:
            raise CommandError('Count must be between 1 and 1000')

        numPhotos = Photo.objects.count()
        for i in range(count):
            newPhoto = Photo(title='Number {}'.format(i+numPhotos),
                             price=200,
                             url='https://picsum.photos/id/{0}/400/400?random={1}'.format(i, i+numPhotos))
            newPhoto.save()

        self.stdout.write(self.style.SUCCESS('Successfully created {0} photo{1}'.format(count, 's' if count>1 else '')))
