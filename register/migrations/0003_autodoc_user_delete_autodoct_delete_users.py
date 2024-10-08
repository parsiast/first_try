# Generated by Django 5.0.7 on 2024-08-10 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_autodoct'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='autodoct',
        ),
        migrations.DeleteModel(
            name='users',
        ),
    ]
