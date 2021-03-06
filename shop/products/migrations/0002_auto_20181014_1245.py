# Generated by Django 2.1.1 on 2018-10-14 09:45

from django.db import migrations

CATEGORIES_DATA = [ {'title':'по умолчанию'},
                    {'title':'Одежда'},
                    {'title':'Посуда'} ]

def create_default_categories(apps, schema_editor):
    Category = apps.get_model('products', 'Category')

    for data in CATEGORIES_DATA:
        Category.objects.get_or_create(**data)


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            create_default_categories,
            lambda x, y: (x, y)
        )
    ]
