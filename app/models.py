from django.db import models


class Clients(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'clients'


class Equipment(models.Model):
    client = models.ForeignKey('Clients', on_delete=models.PROTECT)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'equipment'


class Durations(models.Model):
    client = models.ForeignKey('Clients', on_delete=models.PROTECT)
    equipment = models.ForeignKey('Equipment', on_delete=models.PROTECT)
    start = models.TextField()
    stop = models.TextField()
    mode = models.ForeignKey('Modes', on_delete=models.PROTECT)
    minutes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'durations'


class Modes(models.Model):
    name = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modes'
