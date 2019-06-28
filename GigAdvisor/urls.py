# accounts/urls.py
from django.urls import path
from django.views.generic.base import TemplateView # new
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('team/', views.team, name='team'),
    path('home/', views.home, name='home'),
    path('platforms/', views.PlatformListView.as_view(), name='platforms'),
    #path('platforms/new/', views.recensione_new, name='recensioni_new'),
    path('platforms/<int:id>/', views.recensione_new, name='recensioni_new'),
    path('platforms/reviews/<int:id>/', views.recensione_platform, name='recensione_platform'),
]