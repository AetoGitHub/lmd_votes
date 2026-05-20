from django.db import models as m

# Create your models here.

class Feminosa(m.Model):
    name  = m.CharField(max_length=100)
    image = m.URLField()
    