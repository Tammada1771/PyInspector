# Generated by Django 3.2.3 on 2021-06-03 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_user_employeetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='employeeType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employeetype', verbose_name='EmployeeType'),
        ),
    ]