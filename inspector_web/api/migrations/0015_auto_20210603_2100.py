# Generated by Django 3.2.3 on 2021-06-04 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_equipment_equipmentposition'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batteryinspection',
            old_name='cellElectolyteLevel',
            new_name='cellElectrolyteLevel',
        ),
        migrations.RenameField(
            model_name='building',
            old_name='floorCleanGoodcond',
            new_name='floorCleanGoodCond',
        ),
    ]