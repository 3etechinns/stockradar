from django.db import models
from django.contrib.postgres.fields import ArrayField


class Headline(models.Model):
    source = models.CharField(max_length=25)
    headline = models.TextField(primary_key=True)
    keywords = ArrayField(models.TextField(), blank=True)
    fetched_on = models.DateTimeField()
    link = models.TextField()

    class Meta:
        db_table = 'headlines'

    def __str__(self):
        return self.headline


class Keyword(models.Model):
    keyword = models.CharField(max_length=25)
    frequency = models.FloatField()

    class Meta:
        db_table = 'keywords'

    def __str__(self):
        return self.keyword


class Topic(models.Model):
    topic = models.CharField(max_length=25)
    keyword = models.CharField(max_length=25)
    frequency = models.FloatField()

    class Meta:
        db_table = 'topics'

    def __str__(self):
        return self.topic
