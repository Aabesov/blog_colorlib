from rest_framework import generics
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Blog, Category, Tag
from blog.permissions import IsAuthorOrReadOnly
from blog.serializers import BlogSerializer, CategorySerializer, TagSerializer
from blog.paginations import BlogListPagination


class BlogListCreateAPIView(generics.ListCreateAPIView):
    pagination_class = BlogListPagination
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrReadOnly, ]

    def get_queryset(self):
        search = self.request.query_params.get("search")
        queryset = Blog.objects.all()
        if search:
            queryset = queryset.filter(Q(title__icontains=search) |
                                       Q(description__icontains=search) |
                                       Q(category__title__icontains=search))
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogUpdateDeleteGetAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrReadOnly, ]


class CategoryListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthorOrReadOnly, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagBlogListAPIView(APIView):
    permission_classes = [IsAuthorOrReadOnly, ]

    def get(self, request, pk):
        queryset = Tag.objects.get(id=pk)
        tag_blogs = queryset.tags.all()
        serializers = BlogSerializer(data=tag_blogs, many=True)
        serializers.is_valid()
        return Response(serializers.data)
