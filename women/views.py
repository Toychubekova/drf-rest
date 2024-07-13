from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from women.models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializer import WomenSerializer


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class WomenAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerOrReadOnly,)



class WomenAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)


# class WomenViewSet(viewsets.ModelViewSet):
#     # queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#
#         if not pk:
#             return Women.objects.all()[:3]
#
#         return Women.objects.filter(pk=pk)
#
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name})

# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# class WomenAPIView(APIView):
#     def get(self, request):
#         w = Women.objects.all().values()
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self,request,*args,**kwargs):
#         pk = kwargs.get('pk',None)
#         if not pk:
#             return Response({"error": "Method Put not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exist"})
#
#
#         serializer = WomenSerializer(data = request.data,instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
