# Generated by Django 4.0.4 on 2022-05-11 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvuploader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookID', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=500)),
                ('average_rating', models.FloatField(default=0)),
                ('isbn', models.CharField(max_length=200)),
                ('isbn13', models.CharField(max_length=200)),
                ('language_code', models.CharField(max_length=200)),
                ('num_pages', models.FloatField(max_length=200)),
                ('ratings_count', models.FloatField(default=0)),
                ('text_reviews_count', models.FloatField(default=0)),
                ('publication_date', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
            ],
        ),
    ]
