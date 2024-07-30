import logging
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from post_machine.models import PostMachine, Locker
from django.db.models.signals import post_save
from django.dispatch import receiver

logger = logging.getLogger(__name__)


class Parcel(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.CharField(max_length=200)
    size = models.IntegerField()
    post_machine_recipient = models.ForeignKey(PostMachine, on_delete=models.CASCADE)
    locker = models.ForeignKey(Locker, null=True, blank=True, default=None, on_delete=models.CASCADE)
    order_datetime = models.DateTimeField("date published")
    open_datetime = models.DateTimeField("date published", null=True, blank=True)
    update_datetime = models.DateTimeField("date published", default=datetime.now)
    status = models.BooleanField(
        default=False)  # True- Delivered, false- not delivered (on delivery fill "open_datetime")

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.post_machine_locker = None

    def __str__(self):
        return f" {self.pk} - {self.sender} - {self.recipient}"

    def __repr__(self):
        return f" {self.pk} - {self.sender} - {self.recipient}"

    def to_client(self):
        return {
            'recipient': self.recipient,
            'sender': self.sender,
            'size': self.size,
            'post_machine_recipient': self.post_machine_recipient,
            'order_datetime': self.order_datetime,
            'open_datetime': self.open_datetime,
            'update_datetime': self.update_datetime,
            'status': self.status
        }

    def form_client(self, data):
        self.recipient = data['recipient']
        self.sender = data['sender']
        self.size = data['size']
        self.post_machine_recipient = data['post_machine_recipient']
        self.order_datetime = data['order_datetime']
        self.open_datetime = data['open_datetime']
        self.update_datetime = data['update_datetime']
        self.status = data['status']


@receiver(post_save, sender=Parcel)
def update_status_on_parcel_put_to_locker(sender, instance, created, **kwargs):
    print(instance)
    if instance.status == False:
        if instance.locker is not None:
            parcel_locker = Locker.objects.get(pk=instance.locker.pk)
            parcel_locker.status = False
            parcel_locker.save()
            logger.info(f"update locker status for parsel {instance}")
