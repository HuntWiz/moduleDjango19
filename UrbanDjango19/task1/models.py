from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.CharField(name='username', max_length=100)
    balance = models.DecimalField(max_digits=100, decimal_places=3)
    age = models.IntegerField()

    class Meta:
        verbose_name = 'Покупатели'
        verbose_name_plural = 'Покупатели'


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=20, decimal_places=3)
    size = models.DecimalField(max_digits=30, decimal_places=3)
    description = models.TextField(blank=True)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    class Meta:
        verbose_name = 'Игры'
        verbose_name_plural = 'Игры'
