from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Passwords do not match.')
        if data['role'] not in User.Roles:
            raise serializers.ValidationError('Invalid user role')
        return data

    def create(self, validated_data):
        data = {
            key: value for key, value in validated_data.items() if key not in ('password1', 'password2')
        }
        data['password'] = validated_data['password1']
        user = self.Meta.model.objects.create_user(**data)
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = (
            'id', 'email', 'first_name', 'last_name', 'password1', 'password2', 'role',
        )
        read_only_fields = ('id',)


class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        user_data = UserSerializer(user).data

        for key, value in user_data.items():
            if key != 'id':
                token[key] = value
        return token


class ChangePasswordSerializer(serializers.Serializer):
    model = get_user_model()
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
