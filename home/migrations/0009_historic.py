# Generated by Django 4.2.2 on 2024-01-04 00:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_course_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_app', models.CharField(choices=[('pa', 'PA'), ('pg', 'PG'), ('ps', 'Pascal'), ('bi', "Newton's Binomial")], max_length=2)),
                ('var1', models.FloatField(blank=True, null=True)),
                ('var2', models.FloatField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
