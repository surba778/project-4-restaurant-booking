# Generated by Django 3.2 on 2022-01-29 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'about ',
                'verbose_name_plural': 'about ',
            },
        ),
        migrations.CreateModel(
            name='We_Are_Feane',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'We_Are_Feane ',
                'verbose_name_plural': 'We_Are_Feane ',
            },
        ),
    ]
