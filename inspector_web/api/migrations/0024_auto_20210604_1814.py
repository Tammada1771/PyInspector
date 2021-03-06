# Generated by Django 3.2.3 on 2021-06-04 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_alter_inspection_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inspection',
            name='name',
        ),
        migrations.AlterField(
            model_name='battery',
            name='inspection',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.inspection', verbose_name='Inspection'),
        ),
        migrations.AlterField(
            model_name='batteryinspection',
            name='inspection',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.inspection', verbose_name='Inspection'),
        ),
        migrations.AlterField(
            model_name='building',
            name='inspection',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.inspection', verbose_name='Inspection'),
        ),
        migrations.AlterField(
            model_name='capacitorbank',
            name='inspection',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.inspection', verbose_name='Inspection'),
        ),
        migrations.AlterField(
            model_name='charger',
            name='inspection',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.inspection', verbose_name='Inspection'),
        ),
        migrations.AlterField(
            model_name='circuitswitcher',
            name='inspection',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.inspection', verbose_name='Inspection'),
        ),
        migrations.AlterField(
            model_name='motoroperatedloadbreak',
            name='inspection',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.inspection', verbose_name='Inspection'),
        ),
        migrations.AlterField(
            model_name='oilbreaker',
            name='inspection',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.inspection', verbose_name='Inspection'),
        ),
        migrations.AlterField(
            model_name='sf6breaker',
            name='inspection',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.inspection', verbose_name='Inspection'),
        ),
        migrations.AlterField(
            model_name='station',
            name='inspection',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='InspectionId', to='api.inspection', verbose_name='Inspection'),
        ),
        migrations.AlterField(
            model_name='transformer',
            name='inspection',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.inspection', verbose_name='Inspection'),
        ),
        migrations.AlterField(
            model_name='vacbreakerindoor',
            name='inspection',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.inspection', verbose_name='Inspection'),
        ),
        migrations.AlterField(
            model_name='vacbreakeroutdoor',
            name='inspection',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.inspection', verbose_name='Inspection'),
        ),
        migrations.AlterField(
            model_name='vacreclosersinglephase',
            name='inspection',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.inspection', verbose_name='Inspection'),
        ),
        migrations.AlterField(
            model_name='vacreclosertriplephase',
            name='inspection',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.inspection', verbose_name='Inspection'),
        ),
        migrations.AlterField(
            model_name='yard',
            name='inspection',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.inspection', verbose_name='Inspection'),
        ),
    ]
