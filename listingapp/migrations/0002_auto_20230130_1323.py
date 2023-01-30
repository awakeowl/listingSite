# Generated by Django 3.2 on 2023-01-30 13:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('listingapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenity',
            name='id',
            field=models.UUIDField(default=uuid.UUID('3e036998-435f-41a0-80e3-3a9d039553b4'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='investorprofile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('621da6f7-6b94-4cb7-8de7-7a33a417c7dd'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c5725520-3b3d-41f7-8d0e-9e905d0c9a15'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='morgage',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b7030eae-cd5b-41d2-b830-da7197aacde7'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.UUIDField(default=uuid.UUID('821b1a65-3187-45a5-a1a6-df89827b5d6f'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='property',
            name='id',
            field=models.UUIDField(default=uuid.UUID('433ed6a6-2b22-437a-9eae-83ed04798cb6'), editable=False, primary_key=True, serialize=False),
        ),
    ]