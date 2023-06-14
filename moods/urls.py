from django.urls import path
from moods import views

urlpatterns = [
    path('moods/', views.MoodList.as_view()),
    path('moods/<int:pk>/', views.MoodDetail.as_view())
]