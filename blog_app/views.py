from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Blog
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from .filters import BlogFilter

# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BlogFilter