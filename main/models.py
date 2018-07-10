from django.db import models


class Manager(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    telegram_slug = models.CharField(max_length=50)
    engine_id = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.telegram_slug

class BetStatus(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Bet(models.Model):
    first_side = models.ForeignKey(Manager, related_name='first_side_manager')
    second_side = models.ForeignKey(Manager, related_name='second_side_manager')
    title  = models.CharField(max_length=50, default='Bet')
    note = models.TextField(null=True)
    status = models.ForeignKey(BetStatus)
    result = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_side.telegram_slug + " - " +self.second_side.telegram_slug + " : " + self.title
