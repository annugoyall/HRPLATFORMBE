from django.contrib.auth import logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User


class LoginAPIView(APIView):
    def authenticate(self, request, **credentails):
        user = None
        try:
            user = User.objects.get(username=credentails['username'])
        except Exception as e:
            return None
        if user:
            if credentails['password'] == user.password:
                return user
            else:
                return None

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = self.authenticate(request, username=username, password=password)
        if user is not None:
            dict = {'Message': 'Login successful'}
            if user.employee:
                dict["employee"] = user.employee.id
            if user.candidate:
                dict["candidate"] = user.candidate.id
            return Response(dict, status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
