# Generated by Django 3.2.3 on 2021-06-04 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20210603_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='duration',
            field=models.IntegerField(null=True),
        ),
    ]