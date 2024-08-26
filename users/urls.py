from django.urls import path, include
from rest_framework import routers

from .views import *

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('create_user/', CreateUserView.as_view(), name='create_user'),
    path('users/', UserList.as_view(), name='user-list'),
    # path('users/<int:pk>/', UserUpdate.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDelete.as_view(), name='user-list'),
    # path('api/', include(router.urls)),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
]