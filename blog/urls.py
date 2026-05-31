from django.urls import path
from .views import landing, home, detail, about

urlpatterns = [
    path('', landing, name='landing'),
    path('artikel/', home, name='home'),
    path('article/<int:id>/', detail, name='detail'),
    path('about/', about, name='about'),
]