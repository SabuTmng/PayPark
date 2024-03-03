from rest_framework import serializers
from models.models import *


class MemberSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True, required=True)
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), required=True, )

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email',
                  'is_admin', 'password', 'is_active', "role")
        lookup_field = 'email'
        read_only_fields = ('id', 'is_admin', 'is_active')

    def get_queryset(self):
        if self.role == 'admin' or self.role == 'staff':
            return User.objects.all()
        else:
            return User.objects.get(email=self.email)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def create_admin(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_admin=True,
            is_staff=True
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email',
                  'is_admin', 'is_active', 'role')
        lookup_field = 'email'
        read_only_fields = ('id', 'first_name', 'last_name',
                            'email', 'is_admin', 'is_active', 'role')


class Role(serializers.ModelSerializer):
    class Meta:
        model = Role


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'user', 'parking', 'parking_from', 'parking_to')
        read_only_fields = ('id', 'user', 'parking', 'parking_from', 'parking_to')
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }

    def create(self, validated_data):
        return Booking.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.parking = validated_data.get('parking', instance.parking)
        instance.parking_from = validated_data.get('parking_from', instance.parking_from)
        instance.parking_to = validated_data.get('parking_to', instance.parking_to)
        instance.save()
        return instance


class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = ('id', 'user', 'location', 'latitude', 'longitude')
        read_only_fields = ('id', 'user', 'location', 'latitude', 'longitude')
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }

    def create(self, validated_data):
        return Parking.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.location = validated_data.get('location', instance.location)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.save()
        return instance


class ParkingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingDetail
        fields = ('id', 'parking', 'vechicle_type', 'price_hour')
        read_only_fields = ('id', 'parking', 'vechicle_type', 'price_hour')
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }

    def create(self, validated_data):
        return ParkingDetail.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.parking = validated_data.get('parking', instance.parking)
        instance.vechicle_type = validated_data.get('vechicle_type', instance.vechicle_type)
        instance.price_hour = validated_data.get('price_hour', instance.price_hour)
        instance.save()
        return instance

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'booking', 'total_price')
        read_only_fields = ('id', 'booking', 'total_price')
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }

    def create(self, validated_data):
        return Payment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.booking = validated_data.get('booking', instance.booking)
        instance.total_price = validated_data.get('total_price', instance.total_price)
        instance.save()
        return instance

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'role_name')
        read_only_fields = ('id', 'role_name')
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }