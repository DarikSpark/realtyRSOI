from .models import Flat
from rest_framework.pagination import PageNumberPagination
from .serializers import FlatSerializer, MyFlatSerializer
from rest_framework import generics


class FlatPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class FlatList(generics.ListAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer
    pagination_class = FlatPagination


class FlatDetail(generics.RetrieveAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class MyFlatList(generics.ListCreateAPIView):
    serializer_class = MyFlatSerializer
    pagination_class = FlatPagination

    def get_queryset(self):
        user_id = self.request.REQUEST['user_id']
        return Flat.objects.filter(user_id=user_id)


class MyFlatDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MyFlatSerializer

    def get_queryset(self):
        user_id = self.request.REQUEST['user_id']
        return Flat.objects.filter(user_id=user_id)
