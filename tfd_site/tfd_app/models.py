import datetime
from django.utils import timezone
from django.db import models



# Create your models here.


class Type(models.Model):
    type_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.type_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1)<= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    list_filter = ['pub_date']


class Strain(models.Model):
    type = models.ForeignKey(Type)
    strain_text = models.CharField(max_length=200)
    strain_info = models.TextField(max_length=1080)
    # strain_pic = models.ImageField()
    # pub_date = models.DateTimeField('Date published')
    #
    def __str__(self):
        return self.strain_text
    #
    #
    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1)<= self.pub_date <= now
    #
    # was_published_recently.admin_order_field = 'pub_date'
    # was_published_recently.boolean = True
    # was_published_recently.short_description = 'Published recently?'
    # list_filter = ['pub_date']




