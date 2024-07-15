from django.urls import path

import parcel.views
import post_machine.views

urlpatterns = [
    path('', post_machine.views.post_machine_view),
    path('<machine_id>/', post_machine.views.locker_view)
]
