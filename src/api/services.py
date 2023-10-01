import datetime
from django.db.models import F, Sum
from django.contrib.auth.models import User
from src.education import models
from src.education.models import ProductAccess


def get_lessons_viewed(product: models.Product) -> int:
    return models.ViewLesson.objects.filter(
        lesson__product=product, viewed_time__gte=F("lesson__duration") * 0.8
    ).count()


def get_total_viewed_time(product: models.Product) -> int:
    total_time = models.ViewLesson.objects.filter(lesson__product=product).aggregate(
        Sum("viewed_time")
    )
    viewed_time = total_time["viewed_time__sum"]
    if isinstance(viewed_time, datetime.timedelta):
        return int(viewed_time.total_seconds())
    return 0


def get_total_students(obj) -> int:
    return obj.users.count()


def get_acquisition_percentage(product: models.Product) -> int:
    total_users = User.objects.count()
    product_access_count = ProductAccess.objects.filter(
        product=product
    ).count()
    return (product_access_count / total_users) * 100 if total_users else 0
