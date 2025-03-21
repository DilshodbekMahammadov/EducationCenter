from django.template.context_processors import request
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import *
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100


class MentorListAPIView(ListCreateAPIView):
    serializer_class = MentorSerializer
    queryset = Mentor.objects.all()

class MentorRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MentorSerializer
    queryset = Mentor.objects.all()

class GroupListAPIView(ListCreateAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

    def get_serializer_class(self):
        if self.request.method=='POST':
            return GroupPostSerializer
        return GroupSerializer

class GroupRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

class StudentListAPIView(ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['gender','active']
    search_fields = ['name', 'phone_number']
    ordering_fields = ['gender', 'active', 'age', 'group']
    pagination_class = MyPageNumberPagination

    def get_serializer_class(self):
        if self.request.method=='POST':
            return StudentSerializer
        return StudentSerializer

    def perform_create(self, serializer):
        serializer.save()

class StudentRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def get_object(self):
        obj = self.queryset.get(id=self.kwargs['pk'])
        if obj.aktiv:
            return obj
        raise NotFound(detail="Bunday aktiv student topilmadi!")

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

class BackendGroupListAPIView(ListAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        return Group.objects.filter(mentor__id=2)


