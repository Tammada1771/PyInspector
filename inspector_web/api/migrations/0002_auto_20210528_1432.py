# Generated by Django 3.2.3 on 2021-05-28 14:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobtitle',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='jobtitle',
            name='workgroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.workgroup', verbose_name='WorkGroup'),
        ),
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='workgroup',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='workgroup',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.location', verbose_name='Location'),
        ),
    ]
