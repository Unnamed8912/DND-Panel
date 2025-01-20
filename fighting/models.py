from django.db import models

class Enemie(models.Model):
    name = models.CharField(max_length=50, unique=True)
    max_health = models.IntegerField()
    cur_health = models.IntegerField()
    initiative = models.IntegerField(default=1)
    id_of_fight = models.ForeignKey('Fight', on_delete=models.CASCADE, null=True)
    is_dead = models.BooleanField(default=False)

class Journal(models.Model):
    attacker = models.CharField(max_length=50)
    spell = models.CharField(max_length=100, default='123')
    health = models.IntegerField(null=True, default=5)
    defender = models.CharField(max_length=50)
    id_of_fight = models.ForeignKey('Fight', on_delete=models.CASCADE, null=True)
    is_damage = models.BooleanField(default=True)
    note = models.CharField(max_length=250, default=None, null=True, blank=True)

class Fight(models.Model):
    name = models.TextField(max_length=100, unique=True)
    all_damage = models.IntegerField(default=0)
    all_health = models.IntegerField(default=0)
    count_of_moves = models.IntegerField(default=0)
    is_ended = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
