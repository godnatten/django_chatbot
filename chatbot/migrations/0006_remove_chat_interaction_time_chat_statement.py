# Generated by Django 4.2.7 on 2023-11-18 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0005_alter_chat_interaction_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='interaction_time',
        ),
        migrations.AddField(
            model_name='chat',
            name='statement',
            field=models.CharField(default='1', max_length=100),
        ),
    ]
