# Generated by Django 3.2.3 on 2021-06-01 22:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210531_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacRecloserSinglePhase',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('surgeArrestors', models.CharField(max_length=25, null=True)),
                ('counter', models.IntegerField(null=True)),
                ('bushings', models.CharField(max_length=25, null=True)),
                ('connectionsGoodCond', models.BooleanField(null=True)),
                ('tankGoodCond', models.BooleanField(null=True)),
                ('oilLeaks', models.BooleanField(null=True)),
                ('animalProtectGoodCond', models.BooleanField(null=True)),
                ('potheadGoodCond', models.BooleanField(null=True)),
                ('overallEquipCond', models.CharField(max_length=50, null=True)),
                ('comment', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VacRecloserTriplePhase',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('surgeArrestors', models.CharField(max_length=25, null=True)),
                ('countera', models.IntegerField(null=True)),
                ('counterb', models.IntegerField(null=True)),
                ('counterc', models.IntegerField(null=True)),
                ('bushings', models.CharField(max_length=25, null=True)),
                ('connectionsGoodCond', models.BooleanField(null=True)),
                ('tankGoodCond', models.BooleanField(null=True)),
                ('oilLeaks', models.BooleanField(null=True)),
                ('animalProtectGoodCond', models.BooleanField(null=True)),
                ('potheadGoodCond', models.BooleanField(null=True)),
                ('overallEquipCond', models.CharField(max_length=50, null=True)),
                ('comment', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='battery',
            old_name='cellElectolyteLevel',
            new_name='cellElectrolyteLevel',
        ),
        migrations.AddField(
            model_name='battery',
            name='equipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.equipment', verbose_name='Equipment'),
        ),
        migrations.AddField(
            model_name='batteryinspection',
            name='equipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.equipment', verbose_name='Equipment'),
        ),
        migrations.AddField(
            model_name='building',
            name='equipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.equipment', verbose_name='Equipment'),
        ),
        migrations.AddField(
            model_name='capacitorbank',
            name='equipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.equipment', verbose_name='Equipment'),
        ),
        migrations.AddField(
            model_name='charger',
            name='equipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.equipment', verbose_name='Equipment'),
        ),
        migrations.AddField(
            model_name='motoroperatedloadbreak',
            name='equipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.equipment', verbose_name='Equipment'),
        ),
        migrations.AddField(
            model_name='oilbreaker',
            name='equipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.equipment', verbose_name='Equipment'),
        ),
        migrations.AddField(
            model_name='sf6breaker',
            name='equipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.equipment', verbose_name='Equipment'),
        ),
        migrations.AddField(
            model_name='station',
            name='equipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='StationEquipmentId', to='api.equipment', verbose_name='Equipment'),
        ),
        migrations.AddField(
            model_name='transformer',
            name='equipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.equipment', verbose_name='Equipment'),
        ),
        migrations.AddField(
            model_name='vacbreakerindoor',
            name='equipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.equipment', verbose_name='Equipment'),
        ),
        migrations.AddField(
            model_name='vacbreakeroutdoor',
            name='equipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.equipment', verbose_name='Equipment'),
        ),
        migrations.AddField(
            model_name='yard',
            name='equipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.equipment', verbose_name='Equipment'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StationId', to='api.stations', verbose_name='Station'),
        ),
        migrations.DeleteModel(
            name='VacRecloser',
        ),
        migrations.AddField(
            model_name='vacreclosertriplephase',
            name='equipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.equipment', verbose_name='Equipment'),
        ),
        migrations.AddField(
            model_name='vacreclosertriplephase',
            name='inspection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.inspection', verbose_name='Inspection'),
        ),
        migrations.AddField(
            model_name='vacreclosersinglephase',
            name='equipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.equipment', verbose_name='Equipment'),
        ),
        migrations.AddField(
            model_name='vacreclosersinglephase',
            name='inspection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.inspection', verbose_name='Inspection'),
        ),
    ]
