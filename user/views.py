from django.shortcuts import render

# Create your views here.
# riders/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.shortcuts import get_object_or_404

from .models import Rider
from .serializers import RiderSerializer
from rider.pagination import GlobalPagination
from drf_spectacular.utils import extend_schema, OpenApiParameter





class RiderListCreateAPIView(APIView):
    #parser_classes = (MultiPartParser, FormParser)
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    @extend_schema(
        summary="List Riders",
        parameters=[
            OpenApiParameter(name='page', description='Page number', required=False, type=int),
            OpenApiParameter(name='page_size', description='Items per page', required=False, type=int),
        ],
        responses=RiderSerializer(many=True),
    )
    def get(self, request):
        riders = Rider.objects.all().order_by('-created_at')

        paginator = GlobalPagination()
        paginated_qs = paginator.paginate_queryset(riders, request)

        serializer = RiderSerializer(paginated_qs, many=True)
        return paginator.get_paginated_response(serializer.data)

    @extend_schema(
        summary="Create Rider",
        request=RiderSerializer,
        responses={201: RiderSerializer},
    )
    def post(self, request):
        serializer = RiderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Rider registered successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class RiderDetailAPIView(APIView):
    #parser_classes = (MultiPartParser, FormParser)
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_object(self, pk):
        return get_object_or_404(Rider, pk=pk)

    @extend_schema(summary="Get Rider by ID")
    def get(self, request, pk):
        rider = self.get_object(pk)
        serializer = RiderSerializer(rider)
        return Response(serializer.data)

    @extend_schema(summary="Update Rider", request=RiderSerializer)
    def put(self, request, pk):
        rider = self.get_object(pk)
        serializer = RiderSerializer(rider, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Updated successfully", "data": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(summary="Partial Update Rider", request=RiderSerializer)
    def patch(self, request, pk):
        rider = self.get_object(pk)
        serializer = RiderSerializer(rider, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Partially updated", "data": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(summary="Delete Rider")
    def delete(self, request, pk):
        rider = self.get_object(pk)
        rider.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class RiderListCreateAPIView1(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        riders = Rider.objects.all().order_by('-created_at')

        paginator = GlobalPagination()
        paginated_qs = paginator.paginate_queryset(riders, request)

        serializer = RiderSerializer(paginated_qs, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = RiderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Rider registered successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RiderDetailAPIView1(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get_object(self, pk):
        return get_object_or_404(Rider, pk=pk)

    def get(self, request, pk):
        rider = self.get_object(pk)
        serializer = RiderSerializer(rider)
        return Response(serializer.data)

    def put(self, request, pk):
        rider = self.get_object(pk)
        serializer = RiderSerializer(rider, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Updated successfully", "data": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        rider = self.get_object(pk)
        serializer = RiderSerializer(rider, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Partially updated", "data": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        rider = self.get_object(pk)
        rider.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)