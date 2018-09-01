from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<match>.+)$', views.get_docs, name='get_docs'),
]
