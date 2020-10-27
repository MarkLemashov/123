from django.db import models
from django.db.models.signals import pre_save


class Customer(models.Model):
    name = models.CharField(max_length=60)
    money = models.IntegerField(default=0)

    def buy_car(self, car_id):
        car = Car.objects.get(id=car_id)
        self.money -= car.price
        try:
            self.save()
            car.customer = self;
            car.save()
        except Exception as error:
            print(error)
            self.money = Customer.objects.get(id=self.id).money
            self.save()

    def earn(self, money_earned):
        self.money += money_earned
        self.save()

    def __str__(self):
        return self.name


class Car(models.Model):
    make = models.CharField(max_length=70)
    price = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.make


def customer_pre_save_validation(sender, instance, *args, **kwargs):
    if instance.money < 0:
        raise Exception('Customer does not have enough money.')


pre_save.connect(customer_pre_save_validation, sender=Customer)
