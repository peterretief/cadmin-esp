from django.db import models

from django.utils import timezone

class Client(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    comment = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.fullname


class Product(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    comment = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Status(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)	 	
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Request(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    comment = models.TextField()

    product = models.ForeignKey('Product')
    client = models.ForeignKey('Client')
    status = models.ForeignKey('Status')

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Company(models.Model):
    author = models.ForeignKey('auth.User')
    company_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    POBox = models.TextField()
    telephone = models.CharField(max_length=200)
    fax = models.CharField(max_length=200)
    vat_number = models.CharField(max_length=200)
    registration_number = models.CharField(max_length=200)				
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.company_name
