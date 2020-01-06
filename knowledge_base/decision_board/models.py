from django.db import models

class Selections(models.Model):
    class Meta:
        verbose_name_plural  = 'Разделы'
        verbose_name = 'Раздел'
        ordering = ['title']
   
    def __str__(self):
        return self.title

    title = models.CharField(verbose_name='Название', max_length=100)
    parent = models.ForeignKey('self', verbose_name='Родитель', 
                                        null=True, 
                                        on_delete=models.PROTECT)
    
class Problems(models.Model):
    class Meta:
        verbose_name_plural = 'Проблемы'
        verbose_name = 'Проблема'
        ordering = ['title']

    def __str__(self):
        return self.title
    
    title = models.CharField(verbose_name='Название', max_length=100)
    content = models.TextField(verbose_name='Описание проблемы', 
                                null=True, 
                                blank=True)
    selection = models.ForeignKey(Selections, verbose_name='Раздел',
                                                null=True,
                                                on_delete=models.PROTECT)    

class Solutions(models.Model):
    class Meta:
        verbose_name_plural = 'Решения'
        verbose_name = 'Решение'

    def __str__(self):
        return self.problem.title

    problem = models.ForeignKey(Problems, verbose_name='Проблема',
                                            null=True,
                                            on_delete=models.PROTECT)
    content = models.TextField(verbose_name='Описание решения')
    