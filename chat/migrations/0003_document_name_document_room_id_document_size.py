# Generated by Django 4.2.7 on 2023-12-20 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_document_delete_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='name',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='room_id',
            field=models.CharField(default='as', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='size',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
