# Generated by Django 3.1 on 2020-08-20 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='description',
            field=models.TextField(default=models.CharField(max_length=128)),
        ),
    ]
