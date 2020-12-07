from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from rest_framework import status

# Create your views here.
class ProductListView (APIView):

    def get (self, request):
        products=Product.objects.all ()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post (self, request):

        serializer= ProductSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView (APIView):

    def get (self,request, pid):
        product=Product.objects.get(id=pid)
        # serializer = ProductSerializer(products, many=True)
        serializer = ProductSerializer(product)
        return Response(serializer.data)