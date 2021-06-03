# Generated by Django 3.2.3 on 2021-06-03 22:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_circuitswitcher'),
    ]

    operations = [
        migrations.CreateModel(
            name='OilBreaker',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('operatorCounter', models.IntegerField(null=True)),
                ('compressorHours', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('hydraulicPress', models.IntegerField(null=True)),
                ('airPress', models.IntegerField(null=True)),
                ('moistureDrain', models.BooleanField(null=True)),
                ('tankOilLevel', models.CharField(max_length=25, null=True)),
                ('bushingOilLevel', models.CharField(max_length=25, null=True)),
                ('freeOilSheen', models.BooleanField(null=True)),
                ('oilLeaks', models.CharField(max_length=50, null=True)),
                ('overallPhysCond', models.CharField(max_length=100, null=True)),
                ('comment', models.CharField(max_length=255, null=True)),
                ('equipment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.equipment', verbose_name='Equipment')),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.inspection', verbose_name='Inspection')),
            ],
        ),
    ]