from django.db import models

# Create your models here.

class ItemList(models.Model):
    Category_Name = models.CharField(max_length=20)

    def __str__(self):
        return self.Category_Name

class Items(models.Model):
    Item_Name = models.CharField(max_length=20)
    Description = models.TextField(blank=False)
    Price = models.IntegerField()
    Category = models.ForeignKey(ItemList, related_name='Name', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='Items/')

    def __str__(self):
        return self.Item_Name

class AboutUs(models.Model):
    Description = models.TextField(blank=False)
#
class Feedback(models.Model):
    User_Name = models.CharField(max_length=20)
    Description = models.TextField(blank=False)
    Rating = models.IntegerField()

    def __str__(self):
        return self.User_Name

class BookTable(models.Model):
    Name = models.CharField(max_length=20)
    Phone_Number = models.IntegerField()
    Email = models.EmailField()
    Total_Person = models.IntegerField()
    Booking_Date = models.DateField()

    def __str__(self):
        return self.Name
