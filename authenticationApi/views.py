from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import userSerializer


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    model = User
    queryset = User.objects.all()
    serializer_class = userSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.create_user(username=request.POST['username'],
                                        password=request.POST['password'],
                                        email=request.POST['email'])
        # serialized_user = userSerializer(instance=user)             to print user data in json
        response = {
            'message': 'User created successfully'
        }
        return Response(data=response)

    def delete(self, request, username=None):
        user = User.objects.filter(username=username)
        user.delete()
        response = {
            'message': 'User deleted successfully'
        }
        return Response(data=response)

    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            response = {
                'message': 'Login successful',
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Invalid credentials'})