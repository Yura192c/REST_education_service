from src.education.models import ProductAccess
from rest_framework.permissions import BasePermission, IsAuthenticated


class HasAccessPermission(IsAuthenticated):
    message = "User do not have access to product."

    def has_permission(self, request, view):
        user = request.user
        product = view.kwargs["product"]
        return ProductAccess.objects.filter(
            user__username=user, product__name=product
        ).exists()
