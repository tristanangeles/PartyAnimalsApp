from django.conf.urls import patterns, include, url

from generator import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PartyAnimalsApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.index,name='index'),
    url(r'^minions/$',views.minion_list,name="minions")

   
)