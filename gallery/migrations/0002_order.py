# Generated by Django 2.2.3 on 2019-07-24 04:57

import address.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20160213_1726'),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text="Unique ID associated with a customer's order", primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number can contain up to 15 digits and must follow the following format: '+999999999'", regex='^\\+?1?\\d{9,15}$')])),
                ('print_size', models.CharField(choices=[('4x6', '4"x6"'), ('6x8', '6"x8"'), ('8x10', '8"x10"'), ('10x12', '10"x12"')], default='4x6', help_text='Book availability', max_length=5)),
                ('shipping_cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('address', address.models.AddressField(on_delete='models.CASCADE', to='address.Address')),
                ('photo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery.Photo')),
            ],
        ),
    ]
