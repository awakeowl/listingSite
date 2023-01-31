# Generated by Django 3.2 on 2023-01-31 11:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Amenities',
            },
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('expected_rent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('service_charge', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Morgage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deposit_percentage', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('developer', models.CharField(blank=True, max_length=55, null=True)),
                ('units', models.IntegerField(blank=True, null=True)),
                ('completion_date', models.DateField(blank=True, null=True)),
                ('map_location', models.CharField(blank=True, max_length=255, null=True)),
                ('amenities', models.ManyToManyField(related_name='amenities', to='listingsapp.Amenity')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='listingsapp.location')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('pictures', models.ImageField(upload_to='properties/')),
                ('bedrooms', models.CharField(choices=[('studio', 'studio'), ('1br', '1br'), ('2br', '2br'), ('3br', '3br'), ('4br', '4br'), ('5br', '5br')], max_length=55)),
                ('bathrooms', models.IntegerField()),
                ('size_sqft', models.IntegerField()),
                ('cash_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cash_plan', models.CharField(max_length=255)),
                ('installment_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('installment_plan', models.CharField(max_length=255)),
                ('investor', models.ManyToManyField(blank=True, related_name='property', to='listingsapp.Investor')),
                ('morgage', models.ManyToManyField(blank=True, related_name='property', to='listingsapp.Morgage')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property', to='listingsapp.project')),
            ],
            options={
                'verbose_name_plural': 'Properties',
            },
        ),
    ]