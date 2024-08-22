from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer


# Создание нового пользователя и проверка на дублирование.
class CreateUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')

            existing_user = User.objects.filter(username=username).exists()
            if existing_user:
                return Response(
                    {'error': 'Пользователь с таким именем пользователя уже существует.'},
                    status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Подключение пагинации для определённых запросов.
class UserListPagination(PageNumberPagination):
    page_size = 3  # Количества страниц отображения по умолчанию.
    # Для изменения количества страниц отображения при GET запросе, чем по умолчанию.(&page_size=...)
    page_size_query_param = 'page_size'
    max_page_size = 10000


# Отображение списка всех пользователей: через APIView и ListAPIView.
# class UserList(APIView):
#     def get(self, request):
#         lst = User.objects.all().values()
#         return Response({"username": list(lst)})


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserListPagination  # Подключение пагинации.
