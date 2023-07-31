from django.db import models


class Place(models.Model):
    title = models.CharField(verbose_name='Название',
                             max_length=200)
    point_title = models.CharField(verbose_name='Название метки на карте',
                                   max_length=100)
    place_id = models.CharField(max_length=200)
    description_short = models.TextField(verbose_name='Короткое описание',
                                         blank=True)
    description_long = models.TextField(verbose_name='Подробное описание',
                                        blank=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    img = models.ImageField(verbose_name='Картинка')
    place = models.ForeignKey(Place, on_delete=models.CASCADE,
                              related_name='images')
    position = models.PositiveIntegerField(verbose_name='Позиция',
                                           default=0,
                                           db_index=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.position} {self.place.title}'
