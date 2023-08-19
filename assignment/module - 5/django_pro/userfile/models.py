from django.db import models

# Create your models here.
class Contect(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveSmallIntegerField()
	remark=models.TextField()

	def __str__(self):
		return self.name

class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	address=models.TextField()
	gender=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	profile_pic=models.ImageField(upload_to='image/',default="")

	def __str__(self):
		return self.fname+" "+self.lname
	
class Product_mst(models.Model):
	pbrand=models.CharField(max_length=30)
	pname=models.CharField(max_length=30,default="")

	def __str__(self):
		return self.pbrand
	

class Product_sub_cat(models.Model):
	pname=models.CharField(max_length=30)
	product_price=models.PositiveIntegerField()
	product_image=models.ImageField(upload_to='products/',default="")
	product_model=models.CharField(max_length=30)
	product_ram=models.PositiveIntegerField()

	def __str__(self):
		return self.pname