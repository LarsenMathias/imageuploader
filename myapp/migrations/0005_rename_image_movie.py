# Generated by Django 3.2.6 on 2021-09-09 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_image2_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Movie',
        ),
    ]
