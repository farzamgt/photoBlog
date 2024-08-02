# Generated by Django 5.0.7 on 2024-08-02 07:06

from django.db import migrations


def create_default_categories(apps, schema_editor):
    Category = apps.get_model('posts', 'Category')
    Category.objects.create(name='Car', image='category_images/cars.jpg')
    Category.objects.create(name='Nature', image='category_images/nature.jpg')
    Category.objects.create(name='Food', image='category_images/foods.jpg')

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_category_image_alter_post_image'),  # Replace with the last migration file
    ]

    operations = [
        migrations.RunPython(create_default_categories),
    ]
