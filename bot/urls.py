from django.conf.urls import url
from bot import views
from bot.views import ChatterBotAppView, ChatterBotApiView, cht, createpost
from django.contrib.auth.decorators import login_required
# from bot.views import cht
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    url(r'^$', views.cht, name='mn'),
    url(r'^createpost$', views.createpost),
    url(r'^chat$', login_required(ChatterBotAppView.as_view()), name='main'),
    url(r'^api/chatterbot/', csrf_exempt(ChatterBotApiView.as_view()), name='chatterbot'),

]