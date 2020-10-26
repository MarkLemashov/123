from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=60)
    money = models.IntegerField(default=0)

    def buy_car(self, car_id):
        car = Car.objects.get(id=car_id)
        car.customer = self;
        car.save()

    def __str__(self):
        return self.name


class Car(models.Model):
    make = models.CharField(max_length=60)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.make
