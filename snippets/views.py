
from ast import Delete, arg
from gc import get_referents
from os import nice
from re import I, S
import re
from django.shortcuts import render

# Create your views here.
# Vistas basadas en funciones - Vistas basadas en clases
 # APIView -> genercis.GenerciAPIView - > generics.Retrevi
 # viewset, ModelsViewset

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# # Decoradores en python
# @api_view(['GET', 'POST'])
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         # return JsonResponse(serializer.data, safe=False)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         # data = JSONParser().parse(request)
#         # serializer = SnippetSerializer(data=data)
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# # def snippet_detail(request, pk):
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         # return HttpResponse(status=404)
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         # return JsonResponse(serializer.data)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         # data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         print(request.data, "2345")
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#             # return JsonResponse(serializer.data)
#         # return JsonResponse(serializer.errors, status=400)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         snippet.delete()
#         # return HttpResponse(status=204)
#         return Response(status=status.HTTP_204_NO_CONTENT)
from rest_framework.views import APIView
from django.http import Http404

# class SnippetList(APIView):

#     def get(self, request):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SnippetDetail(APIView):
    # def get_object(self, pk):
    #     try:
    #         return Snippet.objects.get(pk=pk)
    #     except Snippet.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk):
    #     snippet = self.get_object(pk)
    #     serializer = SnippetSerializer(snippet)
    #     return Response(serializer.data)

    # def put(self, request, pk):
    #     snippet = self.get_object(pk)
    #     serializer = SnippetSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import mixins
from rest_framework import generics

# class SnippetList(
#     generics.GenericAPIView,
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin
# ):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class SnippetDetail(generics.GenericAPIView,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     mixins.RetrieveModelMixin
# ):

#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request,*args,**kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Snippet.objects.all()
    serializer_class = SnippetSerializer
