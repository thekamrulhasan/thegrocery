from django.shortcuts import render
from .serializers import *
from .models import *

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class AllProductsViewAccess(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print(request.user)
        return Response({'Sucess: You are authenticated'})

class ProductView(APIView):
    def get(self,request):
        category = self.request.query_params.get('category')
        if category:
            queryset = Products.objects.filter(category__category_name=category)
        else:
            queryset = Products.objects.all()
        serializers = ProductSerializers (queryset, many=True)
        return Response({'count': len(serializers.data), 'data': serializers.data})
