from django.db import models

class Notes(models.Model):
    textData = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)
