from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY =(
    ('Mecanico', 'Mecanico'),
    ('Flotas', 'Flotas'),
    ('Insumos', 'Insumos'),
    ('Herramienta', 'Herramienta'),
    ('Electricos', 'Electricos'),
    
)


class Product(models.Model):
    name=models.CharField(max_length=100, null=True, verbose_name='Nombre')
    category=models.CharField(max_length=20, choices=CATEGORY, null=True, verbose_name='Categoria')
    cantidad= models.PositiveBigIntegerField(null=True)
    class Meta: 
        verbose_name_plural='Product'


    def __str__(self):
        return f'{self.name}'
    
class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE,null=True, verbose_name='Producto')
    staff= models.ForeignKey(User,models.CASCADE,null=True, verbose_name='Personal')
    order_quantity=models.PositiveIntegerField(null=True, verbose_name='Cantidad de Orden')
    date=models.DateTimeField(auto_now_add=True, verbose_name='Fecha')

    class Meta: 
        verbose_name_plural='Order'


    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'

    
