# Generated by Django 4.2 on 2023-05-12 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='bottoms',
        ),
        migrations.RemoveField(
            model_name='match',
            name='tops',
        ),
        migrations.AddField(
            model_name='match',
            name='bottom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.bottom'),
        ),
        migrations.AddField(
            model_name='match',
            name='top',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.top'),
        ),
    ]
