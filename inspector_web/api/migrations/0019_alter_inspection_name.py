# Generated by Django 3.2.3 on 2021-06-04 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_inspection_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
