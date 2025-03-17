from django.template.context_processors import request
from rest_framework.generics import *
from rest_framework.exceptions import NotFound
from .serializers import *

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

    def get_serializer_class(self):
        if self.request.method=='POST':
            return StudentPostSerializer
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