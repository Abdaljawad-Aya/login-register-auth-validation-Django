from django.db import models

# Create your models here.


class Data_Source(models.Model):
    name = models.TextField()

    
class Test_Name(models.Model):
    Name = models.TextField()
    MinValue = models.IntegerField(blank=True ,  null=True)
    MaxValue = models.IntegerField(blank=True ,  null=True)
    Data_Source = models.ForeignKey(Data_Source , on_delete=models.CASCADE )
    Result_Description = models.TextField()

class Data_Set(models.Model):
    Member_ID = models.TextField()
    Result_Name = models.TextField()
    Source = models.TextField()
    Data_Source = models.ForeignKey(Data_Source , on_delete=models.CASCADE)
    Test_Name = models.ForeignKey(Test_Name , on_delete=models.CASCADE )
    Result_Description = models.TextField()
    Numeric_Result = models.IntegerField()
    Patient_DOB = models.DateField()
    Patient_Gender = models.TextField()
    Date_Resulted = models.TextField()



class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=1000, null=True)

	def __str__(self):
		return self.product.name