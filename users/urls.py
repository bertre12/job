from django.urls import path
from .views import CreateUserView, UserList

urlpatterns = [
    path('create_user/', CreateUserView.as_view(), name='create_user'),
    path('users/', UserList.as_view(), name='user-list'),
]