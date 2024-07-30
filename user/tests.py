from django.test import TestCase
from parcel import models as parcel_models, models
from post_machine import models as post_machine_models
from django.test import Client
from django.contrib.auth.models import User


# Create your tests here.
class MyTestCase(TestCase):
    fixtures = ['data']

    def setUp(self):
        test_pmachine = post_machine_models.PostMachine.objects.get(pk=1)
        test_locker = post_machine_models.Locker.objects.filter(post_machine=test_pmachine).all()[0]
        self.test_locker_id = test_locker.pk
        self.test_parcel = parcel_models.Parcel()
        self.test_parcel.recipient = User.objects.create_user(username='test_user', password='test_password')
        self.test_parcel.sender = 'John Doe'
        self.test_parcel.size = 10
        self.test_parcel.post_machine_recipient = test_pmachine
        self.test_parcel.post_machine_locker = test_locker
        self.test_parcel.send_date_time = '2021-01-01 10:00:00'
        self.test_parcel.open_date_time = '2021-01-02 10:00:00'
        self.test_parcel.status = False
        self.test_parcel.save()
        self.test_parcel.post_machine_locker.status = True
        self.test_parcel.post_machine_locker.save()

    def test_something(self):
        actual_locker = post_machine_models.Locker.objects.get(pk=self.test_parcel.post_machine_locker.pk)
        self.assertEqual(actual_locker.status, True)
        c = Client()
        c.login(username='test_user', password='test_password')
        response = c.post(f'/parcel/{self.test_parcel.pk}/')
        self.assertEqual(response.status_code, 302)
        actual_parcel = parcel_models.Parcel.objects.get(pk=self.test_parcel.pk)
        self.assertEqual(actual_parcel.status, True)
        actual_locker = post_machine_models.Locker.objects.get(pk=self.test_parcel.post_machine_locker.pk)
        self.assertEqual(actual_locker.status, False)
