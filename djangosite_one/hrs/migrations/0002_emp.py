# Generated by Django 3.0.3 on 2020-02-09 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('no', models.IntegerField(primary_key=True, serialize=False, verbose_name='Employee No.')),
                ('name', models.CharField(max_length=20, verbose_name='Employee Name')),
                ('job', models.CharField(max_length=10, verbose_name='Job')),
                ('sal', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Salary')),
                ('bon', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Bonus')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hrs.Dept', verbose_name='Department')),
                ('mgr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hrs.Emp', verbose_name='Supervisor')),
            ],
            options={
                'db_table': 'tb_emp',
            },
        ),
    ]
