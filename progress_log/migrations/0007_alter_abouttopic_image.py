# Generated by Django 4.2.3 on 2023-08-10 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress_log', '0006_abouttopic_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abouttopic',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads'),
        ),
    ]