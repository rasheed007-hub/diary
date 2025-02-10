from django.urls import path
from . import views

urlpatterns = [
    path('', views.DiaryList.as_view()),
    path('diary/<int:id>/', views.DiaryDetailView.as_view())
]