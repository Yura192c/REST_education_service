from src.education.models import Product, ProductAccess, ViewLesson
from rest_framework.generics import ListAPIView
from src.api.base.permissions import HasAccessPermission
from .serializers import (ProductLessonViewSerializer, ProductSerializer,
                          StatisticSerializer)


class UserLessonsView(ListAPIView):
    """
    Вывод списка всех уроков по всем продуктам к которым пользователь имеет доступ,
     с выведением информации о статусе и времени просмотра.
    """
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.kwargs["user"]
        return ProductAccess.objects.filter(
            user__username=user
        ).prefetch_related("product__lessons")


class UserProductLessonsView(ListAPIView):
    """
    Вывод списка уроков по конкретному продукту к которому пользователь имеет доступ,
     с выведением информации о статусе и времени просмотра,
      а также датой последнего просмотра ролика.
    """
    permission_classes = [HasAccessPermission]
    serializer_class = ProductLessonViewSerializer

    def get_queryset(self):
        user = self.request.user
        product = self.kwargs["product"]
        return ViewLesson.objects.filter(
            user__username=user, lesson__product__name=product
        ).prefetch_related("lesson")


class ProductStatisticsView(ListAPIView):
    """
    Отображение статистики по продуктам.
     Необходимо отобразить список всех продуктов на платформе
    """
    serializer_class = StatisticSerializer

    def get_queryset(self):
        return Product.objects.all().prefetch_related("lessons")
