from django.urls import reverse
from django.db import models


class Departament(models.Model):
    name = models.CharField('Название отдела', max_length=50, unique=True)

    def __str__(self):
        return self.name


class Rabotnik(models.Model):
    name = models.CharField('Фамилия Имя Отчество', max_length=100)
    post = models.CharField('Должность', max_length=60)
    salary = models.FloatField('Зарплата', null=True, blank=True, )
    departament = models.ForeignKey(Departament, on_delete=models.PROTECT,
        related_name='entries',
        to_field='name',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'WORKER'
        verbose_name_plural = 'WORKERS'
        unique_together = ('name', 'post')

    def __str__(self):
        return "{} {}".format(self.name, self.post)
