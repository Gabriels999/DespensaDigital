from django.contrib.auth.models import User
from django.db import models


class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    fromuser = models.ForeignKey(
        User, null=True, blank=True, related_name="activitylogs_withfromuser", on_delete=models.CASCADE
        )
    jsondata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s / %s / %s' % (
            self.type,
            self.logged_user,
            self.created_at,
        )


class Product(models.Model):
    name = models.CharField(max_length=132)
    price = models.FloatField()
    type_choices = [
        ("CONGELADOS", "Congelados"),
        ("REFRIGERADOS", "Refrigerados"),
        ("HORTIFRUTI", "Hortifruti"),
        ("FRUTAS", "Frutas"),
        ("SECOS", "Secos"),
        ("LIMPEZA", "Limpeza"),
        ("HIGIENE", "Higiene")
    ]
    type = models.CharField(default=False, max_length=64, choices=type_choices)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} | {self.price}"

    def to_dict_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'type': self.type,
        }


class UserStore(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    target_quantity = models.IntegerField()
    real_quantity = models.IntegerField()

    class Meta:
        ordering = ['owner']

    def __str__(self):
        return f"{self.owner.username} | {self.product.name}"

    def to_dict_json(self):
        return {
            'owner': {
                'owner_id': self.owner.id,
                'owner_name': self.owner.username,
            },
            "product": {
                'id': self.product.id,
                'name': self.product.name,
                'price': self.product.price,
                'target_quantity': self.target_quantity,
                'real_quantity': self.real_quantity,
                'type': self.product.type,
                'expected_total': round((self.target_quantity-self.real_quantity)*self.product.price, 2)
            }
        }
