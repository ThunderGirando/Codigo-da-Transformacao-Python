from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    quantity = models.IntegerField(verbose_name="Quantidade")

    class Meta:
        ordering = ['name'] 

    def __str__(self):
        return self.name