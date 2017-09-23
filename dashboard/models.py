from django.db import models
from driver.models import Driver
from customer.models import Customer


class Request(models.Model):

    STATUSES = (
        ('WAITING', 'WAITING'),
        ('ONGOING', 'ONGOING'),
        ('FINISHED', 'FINISHED')
    )

    driver = models.ForeignKey(Driver)
    customer = models.ForeignKey(Customer)
    created_at = models.DateTimeField(auto_now=True)
    accepted_at = models.DateTimeField(null=True)
    status = models.CharField(max_length=30, choices=STATUSES)

