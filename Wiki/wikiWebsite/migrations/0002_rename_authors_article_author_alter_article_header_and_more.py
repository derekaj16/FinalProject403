# Generated by Django 4.1.3 on 2022-12-11 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wikiWebsite", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article",
            old_name="authors",
            new_name="author",
        ),
        migrations.AlterField(
            model_name="article",
            name="header",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="article",
            name="subheader",
            field=models.CharField(max_length=200),
        ),
    ]