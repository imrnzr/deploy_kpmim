# Generated by Django 5.1.3 on 2024-12-16 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('mentorCd', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('mentorName', models.TextField()),
                ('mentorEmail', models.EmailField(default='default@gmail.com', max_length=254)),
            ],
        ),
    ]
