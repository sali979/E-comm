# Generated by Django 3.2.9 on 2021-12-05 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
