# Generated by Django 2.2.3 on 2019-07-25 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]