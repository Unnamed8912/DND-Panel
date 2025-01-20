from django.db import models

class character(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    level = models.IntegerField(default=10)
    klass = models.CharField(max_length=50)
    rasa = models.CharField(max_length=50)
    max_health = models.IntegerField(default=10)
    cur_health = models.IntegerField(default=10)
    description = models.TextField(blank=True, null=True)
    initiative = models.IntegerField(default=0)
    image = models.ImageField(upload_to='character_images', blank=True, null=True, default='character_images/f0c76a8e2cefa7c75ff4328ec491659b_LNOTyCL.jpg')

    class Meta:
        db_table = 'character'
        verbose_name = 'Персонажа'
        verbose_name_plural = 'Персонажи'

