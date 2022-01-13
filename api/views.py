from django.http.response import JsonResponse
from django.shortcuts import render
from api.models import Task
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls= {
        'List':'/task-list/',
        'Detail View': '/task-detail/<str:pk>',
        'Create': '/task-create/',
        'Update':'/task-update/<str:pk>',
        'Delete':'/task-delete/<str:pk>'
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = serializers.taskSerializer(tasks,many= True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request,pk):
    task = Task.objects.get(id=pk)
    serializer = serializers.taskSerializer(task)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = serializers.taskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("Task Successfully created")

@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer = serializers.taskSerializer(instance=task ,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("Task Updated created")

@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item Deleted")
