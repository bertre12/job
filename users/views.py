from django.contrib.auth.models import User
from rest_framework import status, generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


# Создание нового пользователя и проверка на дублирование.

# class CreateUserView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             username = serializer.validated_data.get('username')
#
#             existing_user = User.objects.filter(username=username).exists()
#             if existing_user:
#                 return Response(
#                     {'error': 'Пользователь с таким именем пользователя уже существует.'},
#                     status=status.HTTP_400_BAD_REQUEST)
#
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateUserView(generics.CreateAPIView):  # Создание нового пользователя для всех.
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Подключение пагинации для определённых запросов.

class UserListPagination(PageNumberPagination):
    page_size = 5  # Количества страниц отображения по умолчанию.
    # Для изменения количества страниц отображения при GET запросе, чем по умолчанию.(&page_size=...)
    page_size_query_param = 'page_size'
    max_page_size = 10000


#
#
# # Отображение списка всех пользователей: через APIView и ListAPIView.
#
# # class UserList(APIView):
# #     def get(self, request):
# #         lst = User.objects.all().values()
# #         return Response({"username": list(lst)})
#
#
class UserList(generics.ListAPIView):  # Только чтение.
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserListPagination  # Подключение пагинации.


# Изменение данных по id.
# class UserUpdate(generics.UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# Создание, редактирование и удаление после входа в систему.
class UserDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)  # Добавление прав доступа.


# # Универсальная модель для создания, редактирования пользователей.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)  # Добавление прав доступа.

# Вход на страницу сайта.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return render(request, 'users/login.html', {'error_message': 'Пользователь не найден'})

        if user.check_password(password):
            login(request, user)
            return redirect('home')  # Перенаправление на другую страницу после успешного входа.
        else:
            return render(request, 'users/login.html', {'error_message': 'Неверные учетные данные'})

    return render(request, 'users/login.html')


# Домашняя страница сайта до/после входа зарегистрированного пользователя.
def home(request):
    if request.user.is_authenticated:
        username = request.user.username
        context = {'username': username}
    else:
        context = {'username': None}

    return render(request, 'home.html', context)
