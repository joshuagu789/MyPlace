# Generated by Django 4.2.3 on 2023-08-10 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress_log', '0005_abouttopic_date_added_alter_entry_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='abouttopic',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
