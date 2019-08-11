from django.db import models
from django.contrib.postgres.fields import JSONField

class Owner(models.Model):
    Data = JSONField()

    def __str__(self):
        return self.Owner

class Ownerdata(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name



class Campaign(models.Model):
    campaign_id = models.CharField(max_length=150)

    def __str__(self):
        return self.campaign_id



class Urls(models.Model):
    url_name = models.CharField(max_length=150)
    pa = models.CharField(max_length=150)
    da = models.CharField(max_length=150)

    def __str__(self):
        return self.url_name


