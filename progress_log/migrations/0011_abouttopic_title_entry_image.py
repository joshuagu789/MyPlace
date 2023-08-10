# Generated by Django 4.2.3 on 2023-08-10 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress_log', '0010_alter_abouttopic_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='abouttopic',
            name='title',
            field=models.CharField(default='Topic', max_length=200),
        ),
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
