from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=200)
    token = models.CharField(max_length=500, null=True)
    is_admin = models.BooleanField()

    class Meta:
        db_table = 'user_details'
        managed = True
