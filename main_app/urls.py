from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('moment/', views.index, name='index'),
    path('moment/new/', views.create_moment, name='create_moment'),
    path('moment/<int:moment_id>/', views.detail, name='detail'),
    path('moment/<int:moment_id>/delete/', views.delete_moment, name='delete_moment'),
    path('moment/<int:moment_id>/update/', views.update_moment, name='update_moment'),
    path('moment/<int:moment_id>/createfeeling/', views.create_feeling, name='create_feeling')
]