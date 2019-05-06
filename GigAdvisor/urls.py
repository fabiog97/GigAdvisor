# accounts/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('platforms/', views.PlatformListView.as_view(), name='platforms'),
    #path('platforms/new/', views.recensione_new, name='recensioni_new'),
    path('platforms/<int:id>/', views.recensione_new, name='recensioni_new'),
    path('platforms/reviews/<int:id>/', views.recensione_platform, name='recensione_platform'),
]