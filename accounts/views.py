from re import I
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, CheckSerializer, CompleteUserSerializer
from rest_framework.response import Response
from rest_framework import status


User = get_user_model()

# Register view


class CheckView(viewsets.ViewSet):
    # Returns a json with false if
    # current user is nor a super user
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = User.objects.all().filter(pk=request.user.pk).first()
        serializer = CheckSerializer(queryset)

        return Response(serializer.data)


class RegisterView(viewsets.ModelViewSet):
    """ 
    Class Register View
    Defines the view set for the serializer
    wich register a new user 
    """

    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UpdateProfileView(viewsets.ViewSet):
    """
    Update profile view 
    In this view you can
    """

    permission_classes = [IsAuthenticated]

    def update(self, request, pk):
        user = get_object_or_404(User, pk=pk)

        if request.user != user:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = CompleteUserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            user.save()
            return Response(serializer.data)

        return Response(staus=status.HTTP_400_BAD_REQUEST)
