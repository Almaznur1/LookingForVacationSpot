from django.db import models


class Place(models.Model):
    title = models.CharField(verbose_name='Название',
                             max_length=200)
    description_short = models.TextField(verbose_name='Короткое описание',
                                         blank=True)
    description_long = models.TextField(verbose_name='Подробное описание',
                                        blank=True)
    lng = models.FloatField(verbose_name='Широта')
    lat = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title
