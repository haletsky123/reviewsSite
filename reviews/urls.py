from django.urls import path

from . import views

urlpatterns = [
    path('<int:review_id>/', views.detail, name='detail'),
    path('', views.index, name='index'),
]