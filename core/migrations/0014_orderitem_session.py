# Generated by Django 3.1.2 on 2021-04-21 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210419_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='session',
            field=models.CharField(max_length=32, null=True),
        ),
    ]