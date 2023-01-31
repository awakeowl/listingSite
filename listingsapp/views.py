from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from listingsapp.serializers import LocationSerializer, ProjectSerializer, AmenitySerializer, PropertySerializer, InvestorSerializer, MorgageSerializer
from listingsapp.models import Location, Project, Property, Amenity, Investor, Morgage


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]


class AmenityViewSet(ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    permission_classes = [IsAuthenticated]


class InvestorViewSet(ModelViewSet):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
    permission_classes = [IsAuthenticated]


class MorgageViewSet(ModelViewSet):
    queryset = Morgage.objects.all()
    serializer_class = MorgageSerializer
    permission_classes = [IsAuthenticated]
