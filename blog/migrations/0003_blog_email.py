# Generated by Django 2.2.3 on 2019-08-07 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190807_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
