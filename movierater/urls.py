from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', obtain_auth_token),
<<<<<<< HEAD
    path("api-auth/",
         include("rest_framework.urls")),
]
=======
]
>>>>>>> 3afca6c2a2eb7b733f6b361c20c76d681fc4aa85
