from django.urls import path
from .views import ProdutoList, ProdutoDetail

urlpatterns = [
    path('produtos/', ProdutoList.as_view()),
    path('produtos/<int:pk>/', ProdutoDetail.as_view()),
    path('filter/<str:query>', filter, name="filter-produtos"),
]