# Generated by Django 3.0.5 on 2020-05-03 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
    ]