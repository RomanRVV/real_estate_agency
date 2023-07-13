# Generated by Django 2.2.24 on 2023-07-13 20:08

from django.db import migrations


def add_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        owner, created = Owner.objects.get_or_create(name=flat.owner,
                                                     phonenumber=flat.owners_phonenumber,
                                                     pure_phone=flat.owner_pure_phone)
        owner.flats.set([flat])


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0010_auto_20230713_2236'),
    ]

    operations = [
        migrations.RunPython(add_flats)
    ]
