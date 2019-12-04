import datetime as d


from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length = 200)
    rating = models.FloatField(
        validators =[MinValueValidator(0.0), MaxValueValidator(5.0)])
    year = models.IntegerField(
        validators =[MinValueValidator(1980), MaxValueValidator(int(d.datetime.now().year))]
    )

    class Meta:
        db_table = 'movies'
        managed = True