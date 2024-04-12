from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.serializers import UserLoginSerializer, UserSerializer


class AuthenticationRootView(APIView):
    def get(self, request):
        return Response({
            "apis": {
                "login": {
                    "Type": "POST",
                    "EndPoint": "http://127.0.0.1:8000/api/authentication/login",
                },
            },
        }, status=status.HTTP_200_OK)


class UserLogin(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                "data": {
                    'access_token': str(refresh.access_token),
                    'refresh_token': str(refresh),
                },
                'user': user.username
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response({'message': 'This request is supposed to be a POST Request'},
                        status=status.HTTP_400_BAD_REQUEST)


class UserRegister(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data,
                             "message": "registration successful"},
                            status=status.HTTP_201_CREATED)
        return Response(
            {"data": serializer.errors,
             "message": "Some error occured"},
            status=status.HTTP_400_BAD_REQUEST)
