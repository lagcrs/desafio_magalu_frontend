import uuid

from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# TODO: implement image field
# TODO: implement user foreing key
# TODO: implement category field


'''class Sellers(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name'''




class Products(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    public_id = models.UUIDField(unique=True,
                                 default=uuid.uuid4,
                                 editable=False)
    product_code = models.CharField(max_length=255, blank=False, null=False)
    title = models.CharField(max_length=255, blank=False, null=False)
    # image = cloudinary.models.CloudinaryField('image', null=True)
    quantity = models.PositiveIntegerField(
        validators=[MaxValueValidator(10000)], blank=False, null=False)
    unit_price = models.DecimalField(max_digits=18,
                                     decimal_places=2,
                                     blank=False,
                                     null=False)
    STATUS_CHOICE = (("available", "Disponível"),
                     ("unavailable", "Indisponível"), ("deleted", "Deletado"))
    status = models.CharField(default="unavailable",
                              max_length=20,
                              choices=STATUS_CHOICE)


    categories = (('Tecnologia', 'Tecnologia'), ('Perfumaria', 'Perfumaria'),
                  ('Vestuário', 'Vestuário'), ('Eletrodomésticos',
                                               'Eletrodomésticos'),
                  ('Mercado', 'Mercado'), ('Decoração', 'Decoração'),
                  ('Petshop', 'Petshop'), ('Móveis', 'Móveis'), ('Papelaria',
                                                                 'Papelaria'))
    category = models.CharField(max_length=20,
                                choices=categories,
                                null=False,
                                default="Sem categorias")

    def __str__(self):
        return f"[{self.public_id}: {self.title}]"

    def update_status(self):
        if self.quantity > 0:
            self.status = "available"
        else:
            self.status = "unavailable"

    def set_deleted_status(self):
        self.status = "deleted"

    class Meta:
        ordering = ['-created_at']
