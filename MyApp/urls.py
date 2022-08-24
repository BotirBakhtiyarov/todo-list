from django.urls import path, include
from . import views

urlpatterns = [
    path('new_post',views.TodoCreateView.as_view(), name='new'),
    path('',views.IndexListView.as_view(), name='index'),
    path('delete/<int:pk>',views.TodoDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>',views.TodoUpdateView.as_view(), name='edit'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
