from django.db import models
from django.urls import reverse




class Travel(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Nomi'
    )
    content = models.TextField(
        blank=True,
        verbose_name='Kontent'
    )
    built_at = models.DateField(
        verbose_name='Barpo qilingan vaqti'
    )
    updated_at = models.DateField(
        verbose_name='Yangilangan vaqti'
    )
    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d/',
        verbose_name='Rasm',
        blank=True
    )
    region = models.ForeignKey(
        'Region',
        on_delete=models.PROTECT,
        verbose_name='Viloyat',
    )
    views = models.IntegerField(
        default=0
    )

    def get_absolute_url(self):
        return reverse(
            'view_news',
            kwargs={
                'pk': self.pk
            })


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Joy nomi'
        verbose_name_plural = 'Joy nomlari'
        ordering = ['-built_at']


class Region(models.Model):
    name = models.CharField(
        max_length=50,
        db_index=True,
        verbose_name='Viloyat nomi'
    )

    def get_absolute_url(self):
        return reverse('regi0ns', kwargs={'region_id': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Viloyati'
        verbose_name_plural = 'Viloyatlar'
        ordering = ['name']