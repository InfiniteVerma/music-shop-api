from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=500)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    class Meta:
        abstract = True
    
    name = models.CharField(
        max_length=100,
    )
    price = models.PositiveIntegerField(
        help_text='in rs',
    )

    def __str__(self):
        return self.name
    
class Instrument(Product):
    TYPE_GUITAR = 'guitar'
    TYPE_PIANO = 'piano'
    TYPE_FLUTE = 'flute'
    TYPE_KEYB = 'keyb'
    TYPE_DRUM = 'drum'
    TYPE_CHOICES = (
        (TYPE_GUITAR, 'Guitar'),
        (TYPE_PIANO, 'Piano'),
        (TYPE_FLUTE, 'Flute'),
        (TYPE_KEYB, 'keyb'),
        (TYPE_DRUM, 'drum')
    )
    # name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    typeOfIns = models.CharField(
        max_length=20,
        choices = TYPE_CHOICES
    )
    # price = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class Book(Product):
    # price = models.PositiveIntegerField()
    publisher = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=100)
    addr = models.TextField()
    pno = models.PositiveSmallIntegerField()
    timing = models.CharField(max_length=100)
    closedOn = models.CharField(max_length=100)
    mapLink = models.CharField(max_length=100)

    def __str__(self):
        return self.name
