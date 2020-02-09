from django.db import models

# Create your models here.
class Subject(models.Model):
    """Subjects"""
    no = models.IntegerField(primary_key = True, verbose_name = 'No.')
    name = models.CharField(max_length =20, verbose_name = 'Name')
    intro = models.CharField(max_length = 511, verbose_name = 'Introduction', default ='')
    create_date = models.DateField(null=True, verbose_name ='Date of Creation')
    is_hot = models.BooleanField(default=False, verbose_name = 'Popularity')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_subject'
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

class Teacher(models.Model):
    """Teacher"""
    no = models.IntegerField(primary_key =True, verbose_name ='No.')
    name = models.CharField(max_length = 20, verbose_name = 'Name')
    detail = models.CharField(max_length=1023, default ='', blank = True, verbose_name='Details')
    photo = models.CharField(max_length=1023, default='', verbose_name = 'Photo')
    good_count = models.IntegerField(default=0, verbose_name='Good No.')
    bad_count = models.IntegerField(default=0, verbose_name ='Bad No.')
    subject = models.ForeignKey(Subject, on_delete = models.PROTECT, verbose_name='Belongs to')

    class Meta:
        db_table = 'tb_teacher'
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
