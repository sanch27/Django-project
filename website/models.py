from django.db import models


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")

class Course(models.Model):
	coursename = models.CharField(max_length=45)
	coursedescription = models.CharField(max_length=250)

	def __str__(self):
		return(f"{self.coursename}")


class Package(models.Model):
	packagename = models.CharField(max_length=45)
	packagedescription = models.CharField(max_length=250)
	packageprice = models.CharField(max_length=250)

	def __str__(self):
		return(f"{self.packagename}")

class PackageOptions(models.Model):
    OptionID = models.AutoField(primary_key=True)
    packageid = models.ForeignKey('Package', on_delete=models.CASCADE)
    courseid = models.ForeignKey('Course', on_delete=models.CASCADE)



class Subscription(models.Model):
    SubscriptionID = models.AutoField(primary_key=True)
    recordid = models.ForeignKey('Record', on_delete=models.CASCADE)
    packageid = models.ForeignKey('Package', on_delete=models.CASCADE)
    PaymentDate = models.DateField()
    ExpiryDate = models.DateField()
	
def __str__(self):
		return (f"SubscriptionID: {self.SubscriptionID}, recordid: {self.recordid}, packageid: {self.packageid}, PaymentDate: {self.PaymentDate}, ExpiryDate: {self.ExpiryDate}")