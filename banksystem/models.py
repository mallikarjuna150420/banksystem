from django.db import models
import uuid
from django.core.validators import MaxValueValidator


class CustomersModel(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, )
    acc_number = models.BigIntegerField()
    cust_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    ifsc_code = models.CharField(max_length=10)
    total_amt = models.BigIntegerField(default=100)
