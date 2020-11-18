from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   RetrieveModelMixin, UpdateModelMixin,
                                   DestroyModelMixin)
from rest_framework.viewsets import GenericViewSet
from .models import Products, Sellers
from .serializers import ProductsSerializer, SellersSerializer, UserSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView


class SellersView(
        GenericViewSet,  # generic view functionality
        CreateModelMixin,  # handles posts
        RetrieveModelMixin, # handles gets for 1 seller
        UpdateModelMixin, # handles puts and patches
        ListModelMixin): 


    serializer_class = SellersSerializer
    queryset = Sellers.objects.all()




class ProductsView(
        GenericViewSet,  # generic view functionality
        CreateModelMixin,  # handles posts
        RetrieveModelMixin,  # handles gets for 1 product
        UpdateModelMixin,  
        ListModelMixin,  # handle gets for all products
        DestroyModelMixin):  # handle deletes
    serializer_class = ProductsSerializer
    queryset = Products.objects.exclude(status="deleted")

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance,
                                         data={"status": "deleted"},
                                         partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(status=status.HTTP_204_NO_CONTENT)



class SignUpView(APIView):
    def post(self, request):
        user_to_register = UserSerializer(data=request.data)

        if user_to_register.is_valid():
            user = user_to_register.save()
            # When we save the 'User' model through the serializer,
            # Django does not call the password encryption method.
            # In order for the password to be encrypted, we need
            # to perform the method below.
            user.set_password(user.password)
            user.save()

            token = Token.objects.create(user=user)

            response_data = {
                'status': 'success',
                'payload': {
                    'user': {
                        'id': user.id,
                        'token': token.key,
                    },
                },
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        response_data = {
            'status': 'fail',
            'payload': user_to_register.errors,
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class SignInView(APIView):
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        # Lol
        if not username or not password:
            response_data = {
                'status': 'fail',
                'payload': {
                    'username': ['A username is required.'],
                    'password': ['A password is required.'],
                },
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)

            response_data = {
                'status': 'success',
                'payload': {
                    'user': {
                        'id': user.id,
                        'token': token.key,
                    },
                },
            }
            return Response(response_data, status=status.HTTP_200_OK)

        response_data = {
            'status': 'fail',
            'payload': None,
        }
        return Response(response_data, status=status.HTTP_403_FORBIDDEN)