from django.urls import path

from rest_framework.routers import DefaultRouter

from listingsapp import views

routes = DefaultRouter()
routes.register('locations', views.LocationViewSet, basename='locations')
routes.register('projects', views.ProjectViewSet, basename='projects')
routes.register('properties', views.PropertyViewSet, basename='properties')
routes.register('amenities', views.AmenityViewSet, basename='amenities')
routes.register('investors', views.InvestorViewSet, basename='investors')
routes.register('morgages', views.MorgageViewSet, basename='morgages')

urlpatterns = []
urlpatterns += routes.urls
