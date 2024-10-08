# Generated by Django 5.0.7 on 2024-08-22 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_remove_propertyimage_image_propertyimage_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='photo1',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='photo2',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='photo3',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='PropertyImage',
        ),
    ]
