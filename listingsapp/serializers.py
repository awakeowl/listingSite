from rest_framework import serializers

from listingsapp.models import Location, Project, Property, Amenity, Investor, Morgage


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = "__all__"


class AmenitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Amenity
        fields = "__all__"


class InvestorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Investor
        fields = "__all__"


class MorgageSerializer(serializers.ModelSerializer):
    deposit_amount = serializers.ReadOnlyField()
    balance_percentage = serializers.ReadOnlyField()
    balance_amount = serializers.ReadOnlyField()
    balance_15_years = serializers.ReadOnlyField()
    balance_20_years = serializers.ReadOnlyField()

    class Meta:
        model = Morgage
        fields = "__all__"

    def get_deposit_amount(self, obj):
        return obj.deposit_amount

    def get_balance_percentage(self, obj):
        return obj.balance_percentage

    def get_balance_amount(self, obj):
        return obj.balance_amount

    def get_balance_15_years(self, obj):
        return obj.balance_15_years

    def get_balance_20_years(self, obj):
        return obj.balance_20_years
