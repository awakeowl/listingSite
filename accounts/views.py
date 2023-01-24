from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, views, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator

from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING

from accounts.permissions import IsAdmin
from accounts.serializers import UserSerializer, LoginSerializer, ChangePasswordSerializer

User = get_user_model()


@method_decorator(name='post', decorator=swagger_auto_schema(
    operation_summary="Signup endpoint",
    operation_description="Registers a new user using the provided user details. Returns created user.",
    tags=["User Authentication"],
))
class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = ()
    authentication_classes = ()


@method_decorator(name='post', decorator=swagger_auto_schema(
    operation_summary='Login endpoint',
    operation_description='Authenticates a user using email and password. Returns refresh and access tokens.',
    tags=['User Authentication'],
    responses={status.HTTP_200_OK:  TokenRefreshSerializer},
))
class LoginView(TokenObtainPairView):

    authentication_classes = ()
    permission_classes = ()
    serializer_class = LoginSerializer


@method_decorator(name='post', decorator=swagger_auto_schema(
    operation_summary="Forgot password endpoint",
    operation_description="Takes a user's email address and sends a password reset email if a user with that email exists.",
    tags=["User Authentication"],
    request_body=Schema(
        type=TYPE_OBJECT,
        properties={
            'email': Schema(type=TYPE_STRING, description='string'),
        },
        required=['email'],
    ),
    responses={status.HTTP_200_OK: ""}
))
class ForgotPasswordView(views.APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        try:
            user = User.get_user_by_email(request.data['email'])
            # TODO: Send password reset email

        except (KeyError, User.DoesNotExist):
            pass
        return Response(status=status.HTTP_200_OK)

# FIXME: Not visible on API documentation. Should be converted to APIView?
@method_decorator(name='put', decorator=swagger_auto_schema(
    operation_summary="Change password endpoint",
    operation_description="Sets a new password for a given user and blacklists all associated refresh tokens.",
    tags=["User Authentication"],
    request_body=ChangePasswordSerializer,
    responses={status.HTTP_200_OK: ""}
))
@method_decorator(name='patch', decorator=swagger_auto_schema(
    operation_summary="Change password endpoint",
    operation_description="Sets a new password for a given user and blacklists all associated refresh tokens.",
    tags=["User Authentication"],
    # swagger_auto_schema=None,
    request_body=ChangePasswordSerializer,
    responses={status.HTTP_200_OK: ""}
))
class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.data.get('old_password')
            if not user.check_password(old_password):
                content = {'old_password': 'Wrong password'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.data.get('new_password'))
            user.save()

            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

