# Generated by Django 4.1.3 on 2022-11-03 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='employee_address',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='department',
            name='department',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='Employee.department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee',
            field=models.CharField(default=True, max_length=50),
        ),
    ]