# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import FormParser, MultiPartParser

@swagger_auto_schema(
    method='get',
    operation_description="Retrieve a list of items with status code and message.",
    responses={
         200: openapi.Response(description="Successful retrieval of items"),
         400: "Bad request",
         500: openapi.Response(description="Internal server error"),
         404: openapi.Response(description="Page not found"),
         401: openapi.Response(description="Unauthorized access"),
         403: openapi.Response(description="Forbidden access"),
    }
)
@api_view(['GET'])
def getItemsList(request):
    """
    Get a list of final products.
    """
    try:
            items = Item.objects.filter(item_class_id=4)
            serializer = ItemSerializer(items, many=True)
            response_data = {
                "Success": status.HTTP_200_OK,
                "Message": "Items List Ok.",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
            error_response = {
                "Success": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "Message": f"An error occurred: {str(e)}",
                "data": []
            }
            return Response(error_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@swagger_auto_schema(
    method='get',
    operation_description="Retrieve a list of item classes with status code and message.",
    responses={200: openapi.Response(description="Successful retrieval of items classes"),
               400: "Bad request",
               500: openapi.Response(description="Internal server error"),
               404: openapi.Response(description="Page not found"),
               401: openapi.Response(description="Unauthorized access"),
               403: openapi.Response(description="Forbidden access"),}
)
@api_view(['GET'])
def getItemsClassList(request):
    """
    Get a structured response of all item classes, including status code, message, and data.
    """
    try:
        items_class = ItemsClass.objects.all()
        serializer = ItemsClassSerializer(items_class, many=True)
        response_data = {
            "Success": status.HTTP_200_OK,
            "Message": "Items Class List Ok.",
            "data": serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        error_response = {
            "Success": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "Message": f"An error occurred: {str(e)}",
            "data": []
        }
        return Response(error_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@swagger_auto_schema(
    method='post',
    operation_description="Create a new user with optional details using form data.",
    request_body=MobileEndUserSerializer,  
    consumes=["application/x-www-form-urlencoded", "multipart/form-data"],  
    responses={
        201: openapi.Response(description="User created successfully"),
        400: "Bad request",
        500: openapi.Response(description="Internal server error"),
        404: openapi.Response(description="Page not found"),
        401: openapi.Response(description="Unauthorized access"),
        403: openapi.Response(description="Forbidden access"),
    }
)
@api_view(['POST'])
@parser_classes([FormParser, MultiPartParser])
def create_user(request):
    """
    Create a new user with optional fields.
    """
    try:
        serializer = MobileEndUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "Success": status.HTTP_201_CREATED,
                "Message": "User created successfully.",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "Success": status.HTTP_400_BAD_REQUEST,
                "Message": "Invalid data provided.",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "Success": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "Message": f"An error occurred: {str(e)}",
            "data": []
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@swagger_auto_schema(
    method='get',
    operation_description="Retrieve a list of all mobile end users.",
    responses={200: MobileEndUserSerializer(many=True)}
)
@api_view(['GET'])
def get_mobile_end_users(request):
    """
    Get a list of all mobile end users.
    """
    try:
        users = MobileEndUser.objects.all()
        serializer = MobileEndUserSerializer(users, many=True)
        response_data = {
            "Success": status.HTTP_200_OK,
            "Message": "Mobile End Users List Retrieved Successfully.",
            "data": serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        error_response = {
            "Success": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "Message": f"An error occurred: {str(e)}",
            "data": []
        }
        return Response(error_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
