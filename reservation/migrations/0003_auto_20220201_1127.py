# Generated by Django 3.2 on 2022-02-01 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_alter_reservation_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='number_of_persons',
            new_name='persons',
        ),
    ]
