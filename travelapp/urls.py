from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
#from newtrproject import static

urlpatterns = [
    path('',views.demo,name='demo'),
]

urlpatterns += staticfiles_urlpatterns()