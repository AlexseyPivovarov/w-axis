from django.db import models


# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=20, blank=False, verbose_name=u'name')
    price = models.PositiveIntegerField(verbose_name=u'price')

    def __str__(self):
        return self.name


class Cart(models.Model):

    product = models.ManyToManyField(Product)
    data = models.DateTimeField(auto_now_add=True)
    cost = models.PositiveIntegerField(verbose_name=u'cost', default=0)

    def __str__(self):
        return str(self.data)