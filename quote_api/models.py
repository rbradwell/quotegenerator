from django.db import models

# Create your models here.

class ActorQuote(models.Model):
    id = models.AutoField(primary_key=True)
    actor = models.CharField(max_length=100)
    quote = models.TextField()
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=100)