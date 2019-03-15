from django.db import models

# Create your models here.


class FlowerTypes(models.Model):
    title = models.CharField(max_length= 255,verbose_name='Тип цветка')

    def __str__(self):
        return self.title

class Flower(models.Model):
    type_flower= models.ForeignKey(FlowerTypes, on_delete=models.CASCADE)
    title = models.CharField(max_length= 255,verbose_name='Название')
    price = models.DecimalField(decimal_places=2, max_digits=10000,verbose_name='Цена')
    height = models.FloatField(verbose_name='Высота стебля (м)')
    description = models.TextField(blank=False, null=False,verbose_name='Описание')
    image = models.ImageField(upload_to='flowers_images', verbose_name='Фотография',
                              default='')

    def __str__(self):
        return self.title +" " + str(self.price) + " uah"
