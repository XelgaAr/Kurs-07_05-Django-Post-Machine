from django.contrib import admin
from django.urls import path, include

import post_machine
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', user.views.user_page),
    path('parcel/', include('parcel.urls')),
    path('post_machine/', include('post_machine.urls'))
]
