# Generated by Django 4.2.20 on 2025-04-16 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_published', models.BooleanField(default=False)),
                ('published_date', models.DateField()),
                ('author', models.CharField(max_length=100)),
                ('like_count', models.IntegerField(default=0)),
            ],
        ),
    ]
