# Generated by Django 4.2.7 on 2023-11-18 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0004_alter_chat_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='interaction_time',
            field=models.DurationField(null=True),
        ),
    ]
