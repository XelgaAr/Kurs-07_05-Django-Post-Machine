from django.contrib import admin
from django.urls import path, include

import post_machine
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', user.views.user_page),
    path('login/', user.views.login_view),
    path('logout/', user.views.logout_view),
    path('register/', user.views.register_view),
    path('parcel/', include('parcel.urls')),
    path('post_machine/', include('post_machine.urls'))
]
