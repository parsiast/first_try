# Generated by Django 5.0.7 on 2024-08-21 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_rename_user_usersinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersinfo',
            old_name='pssword',
            new_name='password',
        ),
        migrations.AlterField(
            model_name='usersinfo',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
