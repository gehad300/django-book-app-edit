# Generated by Django 4.0.4 on 2022-04-20 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(max_length=255, upload_to='books/images/'),
        ),
    ]
