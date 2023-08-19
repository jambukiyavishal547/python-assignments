from django.shortcuts import render,redirect
from .models import Contect,User,Product_mst,Product_sub_cat
from django.conf import settings
from django.core.mail import send_mail
import random
# Create your views here.
def index(request):
	return render(request,'index.html')

def add_product(request):
	if request.method=="POST":
		try:
			Product_mst.objects.get(pname=request.POST['pname'])
			msg="Product Alredy Exist"
			return render(request,'add-product.html',{'msg':msg})
		except:
			Product_mst.objects.create(
				pbrand=request.POST['pbrand'],
				pname=request.POST['p_name']
			)
		msg="Product Brand Added Successfully"
		return render(request,'add-product.html',{'msg':msg})
	else:
		return render(request,'add-product.html')

def add_sub_details(request):
	if request.method=="POST":
		try:
			Product_sub_cat.objects.get(pname=request.POST['pname'])
			msg="Product Details Alredy Exist"
			return render(request,'add-sub-details.html',{'msg':msg})
		except Exception as e:
			print(e)
			Product_sub_cat.objects.create(
				pname=request.POST['pname'],
				product_price=request.POST['product_price'],
				product_image=request.POST['product_image'],
				product_model=request.POST['product_model'],
				product_ram=request.POST['product_ram']
			)
			msg="Product Sub Details Add Successfully"
			return render(request,'add-sub-details.html',{'msg':msg})
	else:
		return render(request,'add-sub-details.html')

def view_product(request):
	products=Product_sub_cat.objects.all()
	return render(request,'view-product.html',{'products':products})

def edit_product(request,pk):
	products=Product_sub_cat.objects.get(pk=pk)
	if request.method=="POST":
		products.pname=request.POST['pname'],
		products.product_price=request.POST['product_price'],
		products.product_model=request.POST['product_model'],
		products.product_ram=request.POST['product_ram']
		try:
			products.product_image=request.POST['product_image']
		except:
			pass
		products.save()
		msg="Product Edited"
		return render(request,'edit-product.html',{'msg':msg,'products':products})
	else:
		return render(request,'edit-product.html',{'products':products})


def contect(request):
	if request.method=="POST":
		Contect.objects.create(
			name=request.POST['name'],
			email=request.POST['email'],
			mobile=request.POST['mobile'],
			remark=request.POST['remark'],
			)
		msg="Contect Save Successfully"
		contects=Contect.objects.all().order_by('-id')[:3]
		return render(request,'contect.html',{'msg':msg,'contects':contects})
	else:
		contects=Contect.objects.all().order_by('-id')[:3]
		return render(request,'contect.html',{'contects':contects})

def about(request):
	return render(request,'about.html')

def singup(request):
	if request.method=="POST": 
		try:
			User.objects.get(email=request.POST['email'])
			msg="Email Exist"
			return render(request,'singup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['c_password']:
				User.objects.create(
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						address=request.POST['address'],
						gender=request.POST['gender'],
						password=request.POST['password'],
						profile_pic=request.FILES['profile_pic'],
					)
				msg="User Sing Up Successfully"
				return render(request,'singup.html',{'msg':msg})
			else:
				msg="password not match"
				return render(request,'singup.html',{'msg':msg})
	else:
		return render(request,'singup.html')

def login(request):
	if request.method=="POST":
		try:
			users=User.objects.get(email=request.POST['email'])
			if users.password==request.POST['password']:
				request.session['email']=users.email
				request.session['fname']=users.fname
				request.session['profile_pic']=users.profile_pic.url
				return render (request,'index.html')
			else:
				msg="Incorrect password"
				return render(request,'login.html',{'msg':msg} )
		except Exception as e:
				print(e)
				msg="Email Not Registed"
				return render(request,'login.html',{'msg':msg} )
	else:
		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		return render(request,'login.html')
	except:
		return render(request,'login.html')

def forget_password(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			otp=random.randint(1000,9999)
			subject = 'OTP For forget_password'
			message = f'Hello '+user.fname+", Your OTP For forget_password Is: "+str(otp)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email, ]
			send_mail( subject, message, email_from, recipient_list )
			return render(request ,'otp.html',{'email':user.email,'otp':otp})
		except Exception as e:
			print(e)
			msg="Email Not Registed"
			return render(request,'forget-password.html',{'msg':msg})
	else:
		return render(request,'forget-password.html')

def Verify_otp(request):
	email=request.POST['email']
	otp=request.POST['otp']
	uotp=request.POST['uotp']

	if otp==uotp:
		return render(request,'new-password.html',{'email':email})
	else:
		msg="Incorrect OTP"
		return render(request ,'otp.html',{'email':email,'otp':otp,'msg':msg})

def new_password(request):
	email=request.POST['email']
	np=request.POST['new_password']
	cnp=request.POST['cnew_password']

	if np==cnp:
		user=User.objects.get(email=email)
		user.password=np
		user.save()
		msg="password updated Successfully"
		return render(request,'login.html',{'msg':msg})
	else:
		msg="Password Not Match"
		return render(request,'new-password.html',{'email':email,'msg':msg})

def change_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		if user.password==request.POST['old_password']:
			if request.POST['new_password']==request.POST['cnew_password']:
				user.password=request.POST['new_password']
				user.save()
				return redirect('logout')
			else:
				msg="Password Not Match"
				return render(request,'change-password.html',{'msg':msg})
		else:
			msg="Old Password Not Match"
			return render(request,'change-password.html',{'msg':msg})
	else:
		return render(request,'change-password.html')