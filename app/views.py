from django.shortcuts import render
from .models import *
from .serializer import *
# Create your views here.
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin

class LCStudentApi(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = students.objects.all()
    serializer_class = studentsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class RUDestroyApi(GenericAPIView, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = students.objects.all()
    serializer_class = studentsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    

    