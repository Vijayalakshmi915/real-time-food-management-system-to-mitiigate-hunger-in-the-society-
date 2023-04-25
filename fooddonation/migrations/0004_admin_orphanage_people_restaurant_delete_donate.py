# Generated by Django 4.1.3 on 2022-11-12 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooddonation', '0003_donate_orphavailable_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('adminMobileNo', models.CharField(blank=True, max_length=100, null=True)),
                ('adminMail', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orphanage',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('orphanageMobileNo', models.CharField(blank=True, max_length=100, null=True)),
                ('orphanageMail', models.CharField(blank=True, max_length=100, null=True)),
                ('orphanageLocation', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('peopleMobileNo', models.CharField(blank=True, max_length=100, null=True)),
                ('peopleMail', models.CharField(blank=True, max_length=100, null=True)),
                ('peopleLocation', models.CharField(blank=True, max_length=100, null=True)),
                ('peopleFoodDescription', models.CharField(blank=True, max_length=100, null=True)),
                ('peopleQuantity', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('restaurantMobileNo', models.CharField(blank=True, max_length=100, null=True)),
                ('restaurantMail', models.CharField(blank=True, max_length=100, null=True)),
                ('available_date', models.DateField(blank=True, null=True)),
                ('restaurantLocation', models.CharField(blank=True, max_length=100, null=True)),
                ('restaurantFoodDescription', models.CharField(blank=True, max_length=100, null=True)),
                ('restaurantQuantity', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Donate',
        ),
    ]