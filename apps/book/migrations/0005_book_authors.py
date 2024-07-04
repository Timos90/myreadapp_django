# Generated by Django 5.0.6 on 2024-07-04 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0004_remove_book_authors"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="authors",
            field=models.ManyToManyField(through="book.BookAuthor", to="book.author"),
        ),
    ]
