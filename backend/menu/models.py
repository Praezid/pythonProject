from django.db import models


class Menu(models.Model):
    monday = models.ForeignKey('Day', on_delete=models.PROTECT, related_name='monday')
    tuesday = models.ForeignKey('Day', on_delete=models.PROTECT, related_name='tuesday')
    wednesday = models.ForeignKey('Day', on_delete=models.PROTECT, related_name='wednesday')
    thursday = models.ForeignKey('Day', on_delete=models.PROTECT, related_name='thursday')
    friday = models.ForeignKey('Day', on_delete=models.PROTECT, related_name='friday')
    saturday = models.ForeignKey('Day', on_delete=models.PROTECT, related_name='saturday')
    sunday = models.ForeignKey('Day', on_delete=models.PROTECT, related_name='sunday')

    def __str__(self):
        return f"{self.monday} | {self.tuesday} | {self.wednesday} | {self.thursday} | {self.friday} | {self.saturday} | {self.sunday}"


class Day(models.Model):
    first_dish = models.ForeignKey('FirstDish', on_delete=models.PROTECT, null=True)
    second_dish = models.ForeignKey('SecondDish', on_delete=models.PROTECT, null=True)
    side_dish = models.ForeignKey('SideDish', on_delete=models.PROTECT, null=True)
    salad = models.ForeignKey('Salad', on_delete=models.PROTECT, null=True)
    drink = models.ForeignKey('Drink', on_delete=models.PROTECT, null=True)
    desert = models.ForeignKey('Desert', on_delete=models.PROTECT, null=True)


class FirstDish(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class SecondDish(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class SideDish(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Salad(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Desert(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
