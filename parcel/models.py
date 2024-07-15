from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from post_machine.models import PostMachine

class Parcel(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.CharField(max_length=200)
    size = models.IntegerField()
    post_machine_recipient = models.ForeignKey(PostMachine, on_delete=models.CASCADE)
    order_datetime = models.DateTimeField("date published")
    open_datetime = models.DateTimeField("date published")
    update_datetime = models.DateTimeField("date published",default=datetime.now)
    status = models.BooleanField(default=False)

    def __str__(self):
        pass
    def __repr__(self):
        pass

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

