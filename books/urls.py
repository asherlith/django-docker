from django.urls import path
from .views import allBook, Create, Show,Change

urlpatterns = [
    path('', allBook.as_view(), name='home'),
    path('<int:id>/', Show),
    path('create/', Create.as_view()),
    path('change/<int:id>/',Change)
]
