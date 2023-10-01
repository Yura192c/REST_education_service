from drf_yasg.utils import swagger_serializer_method
from src.education.models import Product, ProductAccess, ViewLesson
from rest_framework import serializers
from .services import (get_lessons_viewed,
                       get_total_students,
                       get_total_viewed_time,
                       get_acquisition_percentage)


class LessonViewSerializer(serializers.ModelSerializer):
    lesson_name = serializers.CharField(source='lesson.name')

    class Meta:
        model = ViewLesson
        fields = ["lesson", "lesson_name", "status", "viewed_seconds"]


class ProductSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()
    product_name = serializers.CharField(source='product.name')

    @swagger_serializer_method(
        serializer_or_field=LessonViewSerializer(many=True)
    )
    def get_lessons(self, obj):
        lessons = ViewLesson.objects.filter(
            user=obj.user,
            lesson__product=obj.product
        ).prefetch_related("lesson").all()
        return LessonViewSerializer(lessons, many=True).data

    class Meta:
        model = ProductAccess
        fields = ["product", "product_name", "lessons"]


class ProductLessonViewSerializer(serializers.ModelSerializer):
    lesson_name = serializers.CharField(source='lesson.name')

    class Meta:
        model = ViewLesson
        fields = ["lesson", "lesson_name", "status", "viewed_seconds", "last_view"]


class StatisticSerializer(serializers.ModelSerializer):
    lessons_viewed = serializers.SerializerMethodField()
    total_viewed_time = serializers.SerializerMethodField()
    total_students = serializers.SerializerMethodField()
    acquisition_percentage = serializers.SerializerMethodField()

    @swagger_serializer_method(serializer_or_field=serializers.IntegerField)
    def get_lessons_viewed(self, obj) -> int:
        return get_lessons_viewed(obj)

    @swagger_serializer_method(serializer_or_field=serializers.IntegerField)
    def get_total_viewed_time(self, obj) -> int:
        return get_total_viewed_time(obj)

    @swagger_serializer_method(serializer_or_field=serializers.IntegerField)
    def get_total_students(self, obj) -> int:
        return get_total_students(obj)

    @swagger_serializer_method(serializer_or_field=serializers.IntegerField)
    def get_acquisition_percentage(self, obj) -> int:
        return get_acquisition_percentage(obj)

    class Meta:
        model = Product
        fields = [
            "name",
            "lessons_viewed",
            "total_viewed_time",
            "total_students",
            "acquisition_percentage",
        ]
