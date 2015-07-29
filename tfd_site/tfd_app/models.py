from django.db import models
from django.utils import timezone
import datetime


# Create your models here.


class Type(models.Model):
    type_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.type_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_escription = 'Published recently?'
    list_filter = ['pub_date']





class Strain(models.Model):
        type = models.ForeignKey(Type)
        strain_text = models.CharField(max_length=200)
        # votes = models.IntegerField(default=0)

        def __str__(self):
            return self.strain_text