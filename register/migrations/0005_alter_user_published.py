# Generated by Django 5.0.7 on 2024-08-10 09:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_delete_autodoc_remove_user_user_id_user_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 10, 9, 22, 41, 570302, tzinfo=datetime.timezone.utc)),
        ),
    ]
