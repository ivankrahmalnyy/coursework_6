from typing import List
from rest_framework import serializers
from ads.models import Comment, Ad

# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою



class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    author_first_name = serializers.CharField(max_length=50, source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(max_length=50, source="author.last_name", read_only=True)
    author_image = serializers.ImageField(read_only=True, source="author.image")

    class Meta:
        model = Comment
        fields = [
            "pk",
            "text",
            "author_id",
            "created_at",
            "author_first_name",
            "author_last_name",
            "ad_id",
            "author_image"
        ]


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", 'image', 'title', 'price', 'description']



class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    author_first_name = serializers.CharField(max_length=50, source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(max_length=50, source="author.last_name", read_only=True)
    phone = serializers.CharField(max_length=10, source="author.phone", read_only=True)

    class Meta:
        model = Ad
        fields = [
            'pk',
            'image',
            'title',
            'price',
            'phone',
            'description',
            'author_first_name',
            'author_last_name',
            'author_id'
        ]
