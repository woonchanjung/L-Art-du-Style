# Generated by Django 4.2 on 2023-05-12 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_match_bottoms_remove_match_tops_match_bottom_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bottom',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='top',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
