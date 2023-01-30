from django.urls import path

from rest_framework.routers import DefaultRouter

from listingapp import views

routers = DefaultRouter()
routers.register('locations', views.LocationViewSet, basename='locations')
routers.register('projects', views.ProjectViewSet, basename='projects')
routers.register('properties', views.PropertyViewSet, basename='properties')
routers.register('amenities', views.AmenityViewSet, basename='amenities')

urlpatterns = [
    # path("")
]
urlpatterns += routers.urls
