# Generated by Django 5.0.6 on 2024-07-10 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0010_alter_book_options_alter_book_authors_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bookauthor",
            options={"verbose_name_plural": "Books and Authors"},
        ),
    ]
