from . import views
from django.urls import re_path


urlpatterns=[
    re_path('^$',views.welcome,name = 'welcome'),
]