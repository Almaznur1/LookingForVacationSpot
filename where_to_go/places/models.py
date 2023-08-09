from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=200,
        unique=True)
    description_short = models.TextField(
        verbose_name='Короткое описание',
        blank=True)
    description_long = HTMLField(
        verbose_name='Подробное описание',
        blank=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class Image(models.Model):
    img = models.ImageField(verbose_name='Картинка',
                            unique=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE,
                              related_name='images')
    position = models.PositiveIntegerField(verbose_name='Позиция',
                                           default=0,
                                           db_index=True,
                                           blank=True)

    class Meta:
        ordering = ['position']
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        unique_together = ['img', 'place']

    def __str__(self):
        return self.place.title
