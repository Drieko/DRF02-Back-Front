from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from .models import Produto
from .serializers import ProdutoSerializer
from drf_yasg.utils import swagger_auto_schema
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from corsheaders.middleware import CorsMiddleware

class ProdutoPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProdutoFilter(filters.FilterSet):
    nome = filters.CharFilter(field_name='nome', lookup_expr='icontains')
    categoria = filters.CharFilter(field_name='categoria__nome', lookup_expr='icontains')

    class Meta:
        model = Produto
        fields = ['nome', 'categoria']

class ProdutoList(APIView):
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['nome', 'categoria']
    filter_class = ProdutoFilter

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Accept'
        return response

    @swagger_auto_schema(
        query_serializer=ProdutoSerializer,
    )
    def get(self, request):
        produtos = Produto.objects.all()
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(produtos, request)
        serializer = ProdutoSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    @swagger_auto_schema(
        request_body=ProdutoSerializer,
    )
    def post(self, request):
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProdutoDetail(APIView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Accept'
        return response

    @swagger_auto_schema(
        query_serializer=ProdutoSerializer,
    )
    def get(self, request, pk):
        try:
            produto = Produto.objects.get(pk=pk)
            serializer = ProdutoSerializer(produto)
            return Response(serializer.data)
        except Produto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=ProdutoSerializer,
    )
    def put(self, request, pk):
        try:
            produto = Produto.objects.get(pk=pk)
            serializer = ProdutoSerializer(produto, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Produto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            produto = Produto.objects.get(pk=pk)
            produto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Produto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=ProdutoSerializer,
    )
    def patch(self, request, pk):
        try:
            produto = Produto.objects.get(pk=pk)
            serializer = ProdutoSerializer(produto, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Produto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)