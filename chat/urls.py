from django.conf.urls import url

from . import views

urlpatterns = [
    url('^join',views.init,name='join'),
]