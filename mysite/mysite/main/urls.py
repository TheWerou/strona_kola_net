from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('<int:pk>', views.personal_view, name='person'),

]
