from django_redis import get_redis_connection
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def is_valid_refresh_token(token):
    redis_conn = get_redis_connection("default")
    refresh_token = RefreshToken(token)
    stored_token = redis_conn.get(refresh_token.payload['user_id'])
    return stored_token.decode() == token


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        user = self.request.user
        refresh_token = request.data.get('refresh')

        # 리디스에서 리프레시 토큰 검증
        if not is_valid_refresh_token(refresh_token):
            return Response({"detail": "토큰이 유효하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        return super().post(request, *args, **kwargs)


class CustomTokenObtainView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            if response.data is not None:
                print(response.data)
                refresh_token = response.data["refresh"]
                token = RefreshToken(response.data["refresh"])
                redis_conn = get_redis_connection("default")
                redis_conn.set(token.payload['user_id'], refresh_token,
                               ex=86400)  # 1 day expiration
        return response
