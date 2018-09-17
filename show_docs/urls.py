from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index\.php$', views.index, name='index'),
    url(r'^(?P<match>.+)/index\.php$', views.get_docs, name='get_docs'),
]
