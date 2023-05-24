from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES = (
    ('AR', 'Arena para gatos'),
    ('JU', 'Juguetes para gatos'),
    ('CO', 'Comida para gatos'),
    ('AC', 'Accesorios para gatos'),
)

DISTRITO_CHOICES = (
('Lima', 'Lima'),
('Áncon', 'Áncon'),
('Ate', 'Ate'),
('Barranco', 'Barranco'),
('Breña', 'Breña'),
('Carabayllo', 'Carabayllo'),
('Chaclacayo', 'Chaclacayo'),
('Chorrillos', 'Chorrillos'),
('Cieneguilla', 'Cieneguilla'),
('Comas', 'Comas'),
('El Agustino', 'El Agustino'),
('Independencia', 'Independencia'),
('Jesús María', 'Jesús María'),
('La Molina', 'La Molina'),
('La Victoria', 'La Victoria'),
('Lince', 'Lince'),
('Los Olivos', 'Los Olivos'),
('Lurigancho', 'Lurigancho'),
('Lurín', 'Lurín'),
('Magdalena del Mar', 'Magdalena del Mar'),
('Miraflores', 'Miraflores'),
('Pachacamac', 'Pachacamac'),
('Pucusana', 'Pucusana'),
('Pueblo Libre', 'Pueblo Libre'),
('Puente Piedra', 'Puente Piedra'),
('Punta Hermosa', 'Punta Hermosa'),
('Punta Negra', 'Punta Negra'),
('Rímac', 'Rímac'),
('San Bartolo', 'San Bartolo'),
('San Borja', 'San Borja'),
('San Isidro', 'San Isidro'),
('San Juan de Lurigancho', 'San Juan de Lurigancho'),
('San Juan de Miraflores', 'San Juan de Miraflores'),
('San Luis', 'San Luis'),
('San Martín de Porres', 'San Martín de Porres'),
('San Miguel', 'San Miguel'),
('Santa Anita', 'Santa Anita'),
('Santa María del Mar', 'Santa María del Mar'),
('Santa Rosa', 'Santa Rosa'),
('Santiago de Surco', 'Santiago de Surco'),
('Surquillo', 'Surquillo'),
('Villa El Salvador', 'Villa El Salvador'),
('Villa María del Triunfo', 'Villa María del Triunfo')
)



class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField()
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=DISTRITO_CHOICES,max_length=50)
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
# STATUS_CHOICES = (
#     ('Pendiente', 'Pendiente'),
#     ('Aceptado', 'Aceptado'),
#     ('Empacado', 'Empacado'),
#     ('En camino', 'En camino'),
#     ('Entregado', 'Entregado'),
#     ('Cancelado', 'Cancelado'),
# )

# class Payment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     amount = models.FloatField()
#     razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
#     razorpay_payment_status = models.CharField(max_length=100, blank=True, null=True)
#     razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
#     paid = models.BooleanField(default=False)


# class OrderPlaced(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product,on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     ordered_date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pendiente")
#     payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default="")
#     @property
#     def total_cost(self):
#         return self.quantity * self.product.discounted_price