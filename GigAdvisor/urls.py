# accounts/urls.py
from django.urls import path
from django.views.generic.base import TemplateView # new
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/new_profile/', views.createProfile, name='new_profile'),
    path('profile/', views.profiloView, name='profile'),
    path('charts/', views.charts, name='charts'),
    path('home/', views.home, name='home'),
    path('platforms/', views.PlatformListView.as_view(), name='platforms'),
    #path('platforms/new/', views.recensione_new, name='recensioni_new'),
    path('platforms/new_review/<int:id>/', views.recensione_new, name='recensioni_new'),
    path('platforms/reviews/<int:id>/', views.recensione_platform, name='recensione_platform'),
    path('platforms/reviews/andamento/<int:id>/', views.andamento_platform, name='andamento'),
]