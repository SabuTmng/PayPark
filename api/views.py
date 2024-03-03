import http.client

from django.http import JsonResponse

from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from models.models import *
from rest_framework.permissions import IsAuthenticated


class Member(APIView):
    """
        create a new member
    """

    def post(self, request):
        print(request.data)
        serializer = MemberSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=http.client.BAD_REQUEST)
        if get_user_model().objects.filter(email=request.data.get('email')).exists():
            return Response({'message': "User with email exists"}, status=http.client.BAD_REQUEST)
        data = ReadUserSerializer(serializer.create(serializer.validated_data)).data
        return Response({'user': data}, status=200)

    """
        get members
    """

    def get(self, request):
        try:
            if self.request.user.role.role_name == 'admin' or self.request.user.role.role_name == 'staff':
                users = get_user_model().objects.all()
                serializer = ReadUserSerializer(users, many=True)
                return Response(serializer.data, status=http.client.OK)
            if request.query_params.get('email'):
                user = get_user_model().objects.get(email=request.query_params.get('email'))
                searilizer = ReadUserSerializer(user)
                return Response(searilizer.data, status=http.client.OK)
        except:
            return Response({'message': "You are not authorized to view this content"}, status=http.client.FORBIDDEN)


class Booking(APIView):
    def post(self, request):
        # by huting book the user's bookign should beestablished
        serializer = BookingSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=http.client.BAD_REQUEST)
        booking = serializer.create(serializer.validated_data)
        return Response({'id': booking.id}, status=http.client.OK)

    def get(self, request):
        try:
            if self.request.user.role.role_name == 'admin' or self.request.user.role.role_name == 'staff':
                bookings = Booking.objects.all()
                serializer = BookingSerializer(bookings, many=True)
                return Response(serializer.data, status=http.client.OK)
        except:
            pass
        if request.query_params.get('id'):
            booking = Booking.objects.get(id=request.query_params.get('id'))
            searilizer = BookingSerializer(booking)
            return Response(searilizer.data, status=http.client.OK)


class Parking(APIView):
    def post(self, request):
        serializer = ParkingSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=http.client.BAD_REQUEST)
        parking = serializer.create(serializer.validated_data)
        parkingDetail = ParkingDetail.objects.create(parking=parking, **request.data)
        return Response({'id': parkingDetail.id}, status=http.client.OK)

    def get(self, request):
        try:
            if self.request.user.role.role_name == 'admin' or self.request.user.role.role_name == 'staff':
                parkings = Parking.objects.all()
                serializer = ParkingSerializer(parkings, many=True)
                return Response(serializer.data, status=http.client.OK)
        except:
            pass
        if request.query_params.get('id'):
            parking = Parking.objects.get(id=request.query_params.get('id'))
            searilizer = ParkingSerializer(parking)
            return Response(searilizer.data, status=http.client.OK)


class Payment(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=http.client.BAD_REQUEST)
        payment = serializer.create(serializer.validated_data)
        return Response({'id': payment.id}, status=http.client.OK)

    def get(self, request):
        try:
            if self.request.user.role.role_name == 'admin' or self.request.user.role.role_name == 'staff':
                payments = Payment.objects.all()
                serializer = PaymentSerializer(payments, many=True)
                return Response(serializer.data, status=http.client.OK)
            if request.query_params.get('id'):
                payment = Payment.objects.get(id=request.query_params.get('id'))
                searilizer = PaymentSerializer(payment)
                return Response(searilizer.data, status=http.client.OK)
        except:
            return Response({'message': "You are not authorized to view this content"}, status=http.client.FORBIDDEN)


class Roles(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            print("on try")
            return JsonResponse({'role': self.request.user.role.role_name}, status=http.client.OK)
        except Exception as e:
            print(e)
            print("on expect")
            roles = list(Role.objects.values())
            return JsonResponse({'roles': roles}, safe=False, status=http.client.OK)
