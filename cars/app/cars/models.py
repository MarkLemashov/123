from django.db import models
from django.db.models.signals import pre_save


class Customer(models.Model):
    name = models.CharField(max_length=60)
    money = models.IntegerField(default=0)
    item_to_purchase = None

    def buy_car(self, car_id):
        car = Car.objects.get(id=car_id)
        self.item_to_purchase = car
        self.save()

    def earn(self, money_earned):
        self.money += money_earned
        self.save()

    def __str__(self):
        return self.name


class Car(models.Model):
    make = models.CharField(max_length=70)
    price = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.make


def customer_pre_save_validation(sender, instance, *args, **kwargs):
    if instance.item_to_purchase is not None:
        if instance.money >= instance.item_to_purchase.price:
            instance.money -= instance.item_to_purchase.price
            instance.item_to_purchase.customer = instance
            instance.item_to_purchase.save()
            instance.item_to_purchase = None
        else:
            raise Exception('Customer does not have enough money.')


pre_save.connect(customer_pre_save_validation, sender=Customer)
