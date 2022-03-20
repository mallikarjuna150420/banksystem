from django.db import models
import uuid
from customers.models import CustomersModel


class Transactions(models.Model):
    transaction_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    send_account = models.BigIntegerField(null=True)
    recv_account = models.BigIntegerField(null=True)
    trans_amt = models.FloatField(null=True, blank=True)

    send_account = models.ForeignKey(
        CustomersModel, related_name="sender", on_delete=models.CASCADE, null=True)
    recv_account = models.ForeignKey(
        CustomersModel, related_name="recevier", on_delete=models.CASCADE, null=True)
    trans_amt = models.BigIntegerField(null=True)

    trans_date_time = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        trans_amt = self.trans_amt
        self.send_account.total_amt -= trans_amt
        self.recv_account.total_amt += trans_amt
        self.send_account.save()
        self.recv_account.save()
        super(Transactions, self).save(*args, **kwargs)
