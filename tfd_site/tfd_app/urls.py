from django.conf.urls import url

from . import views

urlpatterns = [
    # Home Page URL
    url(r'^$', views.Home, name= 'home'),
      # ex: /tfd_app/
    url(r'^index/$', views.Index, name='index'),
    # ex: /tfd_app/5/
    url(r'^(?P<pk>[0-9]+)/$', views.Detail, name='detail'),
    # ex: /tfd_app/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.Results, name='results'),
    # ex: /tfd_app/5/vote/
    #url(r'^(?P<type_id>[0-9]+)/vote/$', views.vote, name='vote'),

]