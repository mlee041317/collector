from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('reviews/', views.reviews, name='reviews'),
    path('moment/', views.index, name='index'),
    path('moment/new/', views.create_moment, name='create_moment'),
    path('moment/<int:moment_id>/', views.detail, name='detail'),
    path('moment/<int:moment_id>/delete/', views.delete_moment, name='delete_moment'),
    path('moment/<int:moment_id/edit/', views.update_moment, name='update_moment'),
    path('moment/<int:moment_id>/feed/', views.new_moment, name='new_moment')
]

