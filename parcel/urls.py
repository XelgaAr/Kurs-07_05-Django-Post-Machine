from django.urls import path

import parcel.views

urlpatterns = [
    path('', parcel.views.parcels_view),
    path('get_parcel/', parcel.views.get_parcel),
    path('parcel_form/<int:obj_id>/', parcel.views.parcel_form_test_update),
    path('<parcel_id>/', parcel.views.one_parcel_view)
]
