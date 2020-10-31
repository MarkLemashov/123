import graphene
from graphene_django import DjangoObjectType
from .models import Car, Customer


class CarType(DjangoObjectType):
    class Meta:
        model = Car
        fields = ("id", "make", "price", "customer")


class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
        fields = ("id", "name", "money")


class Query(graphene.ObjectType):
    all_cars = graphene.List(CarType)
    all_customers = graphene.List(CustomerType)
    customer_by_name = graphene.Field(CustomerType, name=graphene.String(required=True))

    def resolve_all_customers(self, info):
        return Customer.objects.all()

    def resolve_all_cars(self, info):
        return Car.objects.all()

    def resolve_customer_by_name(self, info, name):
        try:
            return Customer.objects.get(name=name)
        except Customer.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
