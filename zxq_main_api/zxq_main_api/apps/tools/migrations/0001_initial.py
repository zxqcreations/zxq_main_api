# Generated by Django 2.2.4 on 2019-08-13 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_series_number', models.CharField(max_length=100)),
                ('data_time', models.CharField(max_length=100)),
                ('data_content', models.TextField()),
            ],
        ),
    ]