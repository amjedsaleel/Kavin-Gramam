# Django
from django.db import models


# Create your models here.


class Member(models.Model):
    """
    Adding members to the charitable trust
    """
    ration_card_status = (
        ('APL', 'APL'),
        ('BPL', 'BPL'),
    )

    name = models.CharField(max_length=30, verbose_name='Name')
    age = models.IntegerField(verbose_name='Age')
    phone = models.PositiveIntegerField(help_text='Enter phone number without country code')
    house_name = models.CharField(max_length=50)
    locality = models.CharField(max_length=50)
    pin_code = models.IntegerField()
    ration_card = models.CharField(choices=ration_card_status, max_length=10)
    annual_income = models.IntegerField()
    job = models.CharField(max_length=50)
    remark = models.TextField(max_length=100, help_text='Max 100 letters', blank=True)

    class Meta:
        unique_together = ('name', 'house_name', 'phone')

    def __str__(self):
        return self.name


class HouseMember(models.Model):
    """
    Its for adding house members details of an member to added to charitable trust
    """
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(blank=True, null=True)
    job = models.CharField(max_length=50, blank=True)
    relationship = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Defines that which type of category are providing. eg:- Food, Medicine etc
    """
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category


class Need(models.Model):
    """
    requirement for a member
    """
    member = models.OneToOneField(Member, on_delete=models.CASCADE,)
    requirement = models.ManyToManyField(Category, blank=True,)
