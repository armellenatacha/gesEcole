# Generated by Django 3.1.7 on 2021-03-12 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionNote', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
