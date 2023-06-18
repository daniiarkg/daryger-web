from django.db import models


# Create your models here.
class User(models.Model):
    photo = models.ImageField(upload_to="media", null=True, blank=True)
    fio = models.CharField(max_length=100, null=True)
    # Other fields are in development stage


class Doc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doc = models.FileField(upload_to="media")


# Other models are in development stage
