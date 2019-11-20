from django.urls import path
from django.views.generic import RedirectView
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('<int:pk>', views.personal_view, name='person'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico')),

]
