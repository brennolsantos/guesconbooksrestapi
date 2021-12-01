from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
                  'email', 'name')
        extra_kwargs = {
            'name': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data['name'],
            zip_code='00000000',
            country='Brazil',
            phone_number='0000000000'
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['is_superuser']


class CompleteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exlude = ['password']
