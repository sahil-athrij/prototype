from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from organisation.models import Organisation


class HsnCode(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    description = models.TextField()
    gst_percent = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])


class BillingProduct(models.Model):
    title = models.CharField(max_length=255)
    product_hsn = models.ForeignKey(HsnCode, on_delete=models.SET_NULL, blank=True, null=True)
    code = models.CharField(max_length=8)
    price = models.FloatField()
    stock = models.IntegerField()
    discount = models.PositiveIntegerField(validators=[MaxValueValidator(100)], default=0)
    price2 = models.FloatField(default=0)
    price3 = models.FloatField(default=0)
    gst_percent = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT)
