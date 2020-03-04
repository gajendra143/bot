from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^registration$', views.userRegistration),
    url(r'^login$', views.userLogin, name='login'),
    url(r'^dashboard$', views.dashBoard),
    url(r'^logout$', views.userLogout, name='logout'),
    url(r'^db_data$', views.data_from_chatbot, name='data_from_chatbot'),

]