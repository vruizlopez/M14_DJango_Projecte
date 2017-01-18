from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^projecteaws220/', include('projecteaws220.urls')),
    url(r'^admin/', admin.site.urls),
]
