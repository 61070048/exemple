# Generated by Django 3.0.5 on 2020-05-03 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
