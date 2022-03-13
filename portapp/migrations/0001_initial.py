# Generated by Django 4.0.3 on 2022-03-13 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
