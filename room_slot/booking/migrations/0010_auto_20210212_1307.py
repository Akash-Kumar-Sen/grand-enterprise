# Generated by Django 3.0.3 on 2021-02-12 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_auto_20210212_1306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apartment',
            old_name='room_image',
            new_name='apartment_image',
        ),
        migrations.RenameField(
            model_name='apartment',
            old_name='room_no',
            new_name='apartment_no',
        ),
        migrations.RenameField(
            model_name='apartment',
            old_name='room_type',
            new_name='apartment_type',
        ),
    ]
