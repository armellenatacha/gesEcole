# Generated by Django 3.1.7 on 2021-03-21 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionNote', '0011_auto_20210320_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='sequence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sequenceNote', to='gestionNote.sequences'),
        ),
    ]
