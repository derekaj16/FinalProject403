# Generated by Django 4.1.3 on 2022-11-17 22:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=30)),
                ('subheader', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wikiWebsite.person')),
                ('dateBecameAuthor', models.DateField(default=datetime.datetime.today)),
            ],
            bases=('wikiWebsite.person',),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wikiWebsite.person')),
                ('dateSubscribed', models.DateField(default=datetime.datetime.today)),
            ],
            bases=('wikiWebsite.person',),
        ),
        migrations.AddField(
            model_name='person',
            name='status',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='wikiWebsite.status'),
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraphText', models.TextField()),
                ('articleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wikiWebsite.article')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentText', models.TextField()),
                ('articleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wikiWebsite.article')),
                ('personID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wikiWebsite.person')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(to='wikiWebsite.person'),
        ),
    ]
