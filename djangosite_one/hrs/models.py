from django.db import models

# Create your models here.
class Dept(models.Model):
    """Department"""
    no = models.IntegerField(primary_key = True,  verbose_name = 'Dept No.')
    name = models.CharField(max_length = 20 , verbose_name = 'Dept Name')
    location = models.CharField(max_length = 10 , verbose_name = 'Dept Location')

    class Meta:
        db_table = 'tb_dept'

    def __str__(self):
        return self.name

class Emp(models.Model):
    """Employee"""
    no = models.IntegerField(primary_key = True, verbose_name = 'Employee No.')
    name = models.CharField(max_length = 20, verbose_name ='Employee Name')
    job = models.CharField(max_length=10, verbose_name='Job')
    # one to many key  (inside table)
    mgr = models.ForeignKey('self', on_delete=models.SET_NULL, null =True, blank =True, verbose_name ='Supervisor')
    sal = models.DecimalField(max_digits = 7, decimal_places=2, verbose_name='Salary')
    bon = models.DecimalField(max_digits = 7, decimal_places=2, null=True, blank=True, verbose_name='Bonus')
    # one to many key (outside table)
    dept = models.ForeignKey(Dept, on_delete = models.PROTECT, verbose_name ='Department')

    class Meta:
        db_table = 'tb_emp'