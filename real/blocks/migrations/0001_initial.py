# Generated by Django 4.0.2 on 2022-02-27 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='photos/blocks/%Y/%m/%d/')),
            ],
        ),
    ]
