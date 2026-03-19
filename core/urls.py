from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'), path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'), path('education/', views.education, name='education'),
    path('contacts/', views.contacts, name='contacts'), path('task1018/', views.task_1018, name='task_1018'),
]
