# Generated by Django 4.2.2 on 2023-12-24 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('abstract', models.TextField()),
                ('content', models.TextField()),
                ('link', models.TextField()),
            ],
        ),
    ]
