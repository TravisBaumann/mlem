from django.conf.urls import url
from . import views
from .forms import LoginForm


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/(?P<id>\d+)/$', views.user_page, name='user_page'),
    url(r'^users/make-post/$', views.make_post, name='make_post'),
    url(r'^login/$', 'django.contrib.auth.views.login', 
        {'authentication_form': LoginForm},
        name='login'),
    url(r'^logout/$', 
        'django.contrib.auth.views.logout', 
        {'template_name': 'registration/logout.html'},
        name='logout'),
    url(r'^register/$', views.register, name='register'),
]