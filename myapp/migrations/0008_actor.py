# Generated by Django 3.2.6 on 2021-09-10 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_controversy'),
    ]

    operations = [
        migrations.CreateModel(
            name='actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='myimage')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
