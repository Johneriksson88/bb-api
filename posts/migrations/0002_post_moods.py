# Generated by Django 3.2.19 on 2023-06-14 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moods', '0002_remove_mood_posts'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='moods',
            field=models.ManyToManyField(related_name='posts', to='moods.Mood'),
        ),
    ]