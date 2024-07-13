from django.shortcuts import render
from rest_framework import generics
from women.models import Women
from .serializer import WomenSerializer


class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
