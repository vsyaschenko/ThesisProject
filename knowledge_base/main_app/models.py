from django.db import models

class Sections(models.Model):
    class Meta:
        verbose_name_plural = 'Области знаний'
        verbose_name = 'Область знаний'
        ordering = ['name']
    
    def __str__(self):
        return self.name

    name = models.CharField(verbose_name='Название', max_length=100)
    content = models.TextField(verbose_name='Описание', null=True, blank=True)
    relevant = models.BooleanField(verbose_name='Действует', default=True)

class Processes(models.Model):
    class Meta:
        verbose_name_plural = 'Процессы'
        verbose_name = 'Процесс'
        ordering = ['name']
    
    def __str__(self):
        return self.name

    name = models.CharField(verbose_name='Название', max_length=100)
    content = models.TextField(verbose_name='Описание', null=True, blank=True)
    relevant = models.BooleanField(verbose_name='Действует', default=True)
    section = models.ForeignKey(Sections, verbose_name='Раздел', null=True,
                                         on_delete=models.PROTECT)

class Problems(models.Model):
    class Meta:
        verbose_name_plural = 'Проблемы'
        verbose_name = 'Проблема'
        ordering = ['-published']
    
    def __str__(self):
        return self.name

    name = models.CharField(verbose_name='Название', max_length=100)
    content = models.TextField(verbose_name='Описание', null=True, blank=True)
    relevant = models.BooleanField(verbose_name='Действует', default=True)
    process = models.ForeignKey(Processes, verbose_name='Процесс',
                                            on_delete=models.PROTECT)
    published = models.DateTimeField(verbose_name='Опубликовано', 
                                        auto_now=True)
    
class Solutions(models.Model):
    class Meta: 
        verbose_name_plural = 'Решения'
        verbose_name = 'Решение'
        ordering = ['-published']
    
    def __str__(self):
        return self.problem.name

    problem = models.ForeignKey(Problems, verbose_name='Проблема', 
                                            on_delete=models.PROTECT)
    content = models.TextField(verbose_name='Описание', null=True, blank=True)
    relevant = models.BooleanField(verbose_name='Действует', default=True)
    published = models.DateTimeField(verbose_name='Опубликовано')

class Settings(models.Model):
    class Meta:    
        verbose_name_plural = 'Настройки по умолчанию'
        verbose_name = 'Настройка по умолчанию'
    
    def __str__(self):
        return self.key

    key = models.CharField(verbose_name='Ключ', max_length=50, 
                                                primary_key=True)
    value = models.CharField(verbose_name='Значение', max_length=100,
                                                        blank=True)
    
