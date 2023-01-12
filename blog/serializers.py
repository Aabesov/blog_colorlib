from rest_framework import serializers

from blog.models import Blog, Category, Tag


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ("author", "updated_at")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["count"] = instance.blogs.count()
        return representation


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
