from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': "User Registration Success!",
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        try:
         refresh_token =  request.data['refresh']
         token = RefreshToken(refresh_token)
         token.blacklist()
         return Response({'message':'Loggout Out'}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'error':'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


