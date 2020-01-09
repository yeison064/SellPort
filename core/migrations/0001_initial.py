# Generated by Django 2.2 on 2019-12-22 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('photo', models.ImageField(upload_to='profile_photo')),
                ('tagline', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=500)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('location', models.CharField(max_length=200)),
                ('locationURL', models.URLField(blank=True, max_length=300)),
                ('twtrLink', models.URLField(blank=True, max_length=300)),
                ('gthbLink', models.URLField(blank=True, max_length=300)),
                ('linkedLink', models.URLField(blank=True, max_length=300)),
                ('instaLink', models.URLField(blank=True, max_length=300)),
                ('mediumLink', models.URLField(blank=True, max_length=300)),
            ],
        ),
    ]