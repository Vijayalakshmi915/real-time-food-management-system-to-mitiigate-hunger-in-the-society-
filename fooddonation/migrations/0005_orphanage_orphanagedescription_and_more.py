# Generated by Django 4.1.3 on 2022-11-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooddonation', '0004_admin_orphanage_people_restaurant_delete_donate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orphanage',
            name='orphanageDescription',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orphanage',
            name='orphanageQuantity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orphanage',
            name='orphavailable_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
