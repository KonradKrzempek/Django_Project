from django.conf.urls import url
from . import views as core_views

urlpatterns = [
    url('', core_views.home, name='home'),
]