from django.db import models
from django.contrib.auth.models import User

class PostMachine(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.address} - {self.city}"

    def __repr__(self):
        return f"{self.address} - {self.city}"

class Locker(models.Model):
    size = models.IntegerField()
    post_machine = models.ForeignKey(PostMachine, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"SIZE : {self.size} - PM {self.post_machine} - {self.status}"

    def __repr__(self):
        return f"SIZE : {self.size} - PM {self.post_machine} - {self.status}"
