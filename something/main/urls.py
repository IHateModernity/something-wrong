from django.urls import path
from .views import main_page, PostCreateView

urlpatterns = [
    path('', main_page, name='main'),
    path('/create-post', PostCreateView.as_view(), name='create-post'),
]
