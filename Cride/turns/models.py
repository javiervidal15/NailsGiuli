import os
from django.db import models
from django.db.models.deletion import PROTECT
from model_utils.managers import InheritanceManager

# Create your models here.


class Day(models.Model):
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name


class DayTurn(models.Model):
    available = models.BooleanField(default=True)
    day = models.ForeignKey(Day,on_delete=models.PROTECT)
    hours = models.ManyToManyField('Hour')

    def __str__(self):
        return self.day.get_name() + " " + str(self.available)

    def natural_key(self):
        return (self.available, self.day, self.hours)

    def is_available(self):
        return self.available

    def get_day(self):
        return self.day

    def get_hours(self):
        return self.hours


class Hour(models.Model):
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return str(self.start) + " - " + str(self.end)

    def natural_key(self):
        return (str(self.start)[0:5],str(self.end)[0:5])

    def get_start(self):
        return str(self.start)[0:5]

    def get_end(self):
        return str(self.end)[0:5]


class Client(models.Model):
    full_name = models.CharField(max_length=254)
    email = models.EmailField()

    def natural_key(self):
        return (self.full_name, self.email)

    def __str__(self):
        return self.full_name

    def get_full_name(self):
        return self.full_name

    def get_email(self):
        return self.email


class TypeUnavailableDay(models.Model):
    name = models.CharField(max_length=50)
    all_services = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    def get_name(self):
        return self.name

    def is_all_services(self):
        return self.all_services

    def natural_key(self):
        return (self.name,self.all_services)


class DayNotAvailable(models.Model):
    date = models.DateField()
    motive = models.ForeignKey(TypeUnavailableDay,on_delete=PROTECT,null=True,blank=True)

    def __str__(self):
        return str(self.date)

class Service(models.Model):
    name = models.CharField(max_length=254)
    duration = models.PositiveIntegerField(default=30)
    price = models.FloatField(default=0, null=True, blank=True)
    max_turn_simultaneous = models.IntegerField(default=1)
    days_turn = models.ManyToManyField(DayTurn)
    max_days = models.IntegerField(default=7)
    day_not_available = models.ManyToManyField(DayNotAvailable)

    def natural_key(self):
        return (self.duration, self.days_turn, self.day_not_available)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_duration(self):
        return self.duration

    def get_price(self):
        return self.price

    def get_max_days(self):
        return self.max_days

    def get_max_turn_simultaneous(self):
        return self.max_turn_simultaneous

    def get_day_not_available(self):
        return self.day_not_available

    def get_days_turn(self):
        return self.days_turn

    def get_day_not_available(self):
        return self.day_not_available

    def set_data(self, name, duration, price, max_turn_simultaneous,max_days):
        self.name = name
        self.duration = duration
        self.price = price
        self.max_turn_simultaneous = max_turn_simultaneous
        self.max_days = max_days

    def delete_day_turn(self):
        self.days_turn.clear()


class StateTurn(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=100)

    objects = InheritanceManager()

    def natural_key(self):
        return (self.name)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def assigned(self,turn):
        pass

    def completed(self,turn):
        pass

    def notassisted(self,turn):
        pass


class Assigned(StateTurn):
    def completed(self, turn):
        pass

    def notassisted(self,turn):
        pass


class Completed(StateTurn):
    pass


class NotAssisted(StateTurn):
    pass


class Turn(models.Model):
    date_turn = models.DateField()
    state = models.ForeignKey(StateTurn,on_delete=PROTECT)
    service = models.ForeignKey(Service,on_delete=PROTECT)
    clients = models.ManyToManyField(Client)
    paid = models.BooleanField(default=False)
    duration = models.IntegerField()
    start = models.CharField(max_length=10)

    def __str__(self):
        return str(self.date_turn)

    def get_service(self):
        return self.service

    def get_clients(self):
        return self.clients

    def get_state(self):
        return self.state

    def get_start(self):
        return str(self.start)[0:5]

    def get_duration(self):
        return self.duration

    def get_date(self):
        return "%i/%i/%i" % (self.date_turn.day,self.date_turn.month,self.date_turn.year)

    def notify_cancel(self):
        email_cancel_turn(self)


class gender_now(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class orientation_now(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class user_now(models.Model):
    email = models.EmailField()
    gender = models.ForeignKey(gender_now,on_delete=PROTECT)
    orientation = models.ForeignKey(orientation_now,on_delete=PROTECT)

    def __str__(self):
        return self.email
