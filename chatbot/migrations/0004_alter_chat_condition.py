# Generated by Django 4.2.7 on 2023-11-15 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0003_chat_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='condition',
            field=models.CharField(max_length=100),
        ),
    ]
