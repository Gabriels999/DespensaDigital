from django.db import models
from django.contrib.auth.models import User

class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    fromuser = models.ForeignKey(User, null=True, blank=True, related_name="activitylogs_withfromuser", on_delete=models.CASCADE)
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
    target_quantity = models.IntegerField()
    real_quantity = models.IntegerField()
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
            'target_quantity': self.target_quantity,
            'real_quantity': self.real_quantity,
            'type': self.type,
        }

    def should_buy(self):
        if self.real_quantity <= self.target_quantity:
            return False
        return True
