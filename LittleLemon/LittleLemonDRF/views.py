# from rest_framework import generics
# from .models import MenuItem, Category
# from .serializers import MenuItemSerializer, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# class CategoryView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
    
# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer
#     ordering_fields = ['title', 'price']
#     filterset_fields = ['title', 'price']
#     search_fields = ['title']
    
@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message":"Some secret message"})

@api_view()
@permission_classes
def manager_view(request):
    return Response({"Only the manager should see this!"})