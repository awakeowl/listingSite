import uuid
from django.db import models


class Location(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4())
    name = models.CharField(max_length=100)
    description = models.TextField()
    # image =

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4())
    name = models.CharField(max_length=100)
    amenities = models.ManyToManyField('Amenity', related_name='amenities')
    location = models.ForeignKey(
        Location, related_name='project', on_delete=models.CASCADE)
    description = models.TextField()
    developer = models.CharField(max_length=55, blank=True, null=True)
    units = models.IntegerField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    map_location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Property(models.Model):

    # class ProperyType(models.TextChoices):
    class Bedrooms(models.TextChoices):
        studio = ('studio', 'studio')
        one_br = ('1br', '1br')
        two_br = ('2br', '2br')
        three_br = ('3br', '3br')
        four_br = ('4br', '4br')
        five_br = ('5br', '5br')

    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4())
    project = models.ForeignKey(
        Project, related_name='property', on_delete=models.CASCADE)
    investor = models.ManyToManyField(
        'InvestorProfile', related_name='property', blank=True)
    morgage = models.ManyToManyField(
        'Morgage', related_name='property', blank=True)
    # property_type = models.
    pictures = models.ImageField(upload_to='properties/')
    bedrooms = models.CharField(max_length=55, choices=Bedrooms.choices)
    bathrooms = models.IntegerField()
    size_sqft = models.IntegerField()
    cash_price = models.DecimalField(max_digits=10, decimal_places=2)
    cash_plan = models.CharField(max_length=255)
    installment_price = models.DecimalField(max_digits=10, decimal_places=2)
    installment_plan = models.CharField(max_length=255)
    # NOTE: SEEK CLARIY: not listed in user provision fields
    # development_status = models.BooleanField(default=False)
    # category

    class Meta:
        verbose_name_plural = "Properties"

    @property
    def price_per_sqft(self):
        return self.price_kes / self.size_sqft

    def __str__(self) -> str:
        return f"{self.project.name} - {self.location.location.name}"


class Morgage(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4())
    price = models.DecimalField(max_digits=10, decimal_places=2)
    deposit_percentage = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def deposit_amount(self) -> int:
        return self.deposit_percentage * self.price

    @property
    def balance_percentage(self) -> int:
        return 100 - self.deposit_percentage

    @property
    def balance_amount(self) -> int:
        return self.balance_percentage * self.price

    @property
    def balance_15_years(self) -> str:
        return "Dummy Response: Seek clarity"

    @property
    def balance_20_years(self) -> str:
        return "Dummy Response: Seek clarity"

    def __str__(self) -> str:
        return f"{self.price}"


class InvestorProfile(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4())
    expected_rent = models.DecimalField(max_digits=10, decimal_places=2)
    service_charge = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)

    @property
    def annual_yield(self, morgage_price: int) -> int:
        return (self.expected_rent * 12)/morgage_price

    @property
    def payback_period(self) -> int:
        return 1/self.annual_yield

    def __str__(self) -> str:
        return f"{self.expected_rent}"


class Amenity(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4())
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Amenities"

    def __str__(self) -> str:
        return self.name
