from rest_framework.permissions import BasePermission, SAFE_METHODS

class AllowGETUnauthenticated(BasePermission):
    """
    GET 요청은 인증되지 않아도 허용. 그 외의 요청은 인증 필요.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated