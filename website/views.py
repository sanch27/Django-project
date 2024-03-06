from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, AddCourseForm, AddPackageForm, AddPackageOptionForm, AddSubscriptionForm
from .models import Record, Course, Package, PackageOptions, Subscription


def home(request):
	records = Record.objects.all()
	courses = Course.objects.all()
	packages = Package.objects.all()
	packageoptions = PackageOptions.objects.all()
	subscriptions = Subscription.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('home')
	else:
		return render(request, 'home.html', {'records':records, 'courses':courses, 'packages':packages, 'packageoptions':packageoptions, 'subscriptions':subscriptions})



def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})



def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')



def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')

# 
	
def customer_course(request, pk):
	if request.user.is_authenticated:
		# Look Up Course
		customer_course = Course.objects.get(id=pk)
		return render(request, 'course.html', {'customer_course':customer_course})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')
	
def delete_course(request, pk):
	if request.user.is_authenticated:
		delete_it = Course.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Course Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def add_course(request):
	form = AddCourseForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_course = form.save()
				messages.success(request, "Course Added...")
				return redirect('home')
		return render(request, 'add_course.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


def update_course(request, pk):
	if request.user.is_authenticated:
		current_course = Course.objects.get(id=pk)
		form = AddCourseForm(request.POST or None, instance=current_course)
		if form.is_valid():
			form.save()
			messages.success(request, "Course Has Been Updated!")
			return redirect('home')
		return render(request, 'update_course.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
	



def customer_package(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_package = Package.objects.get(id=pk)
		return render(request, 'package.html', {'customer_package':customer_package})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')
	
def delete_package(request, pk):
	if request.user.is_authenticated:
		delete_it = Package.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Package Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def add_package(request):
	form = AddPackageForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_package = form.save()
				messages.success(request, "Package Added...")
				return redirect('home')
		return render(request, 'add_package.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


def update_package(request, pk):
	if request.user.is_authenticated:
		current_package = Package.objects.get(id=pk)
		form = AddPackageForm(request.POST or None, instance=current_package)
		if form.is_valid():
			form.save()
			messages.success(request, "Package Has Been Updated!")
			return redirect('home')
		return render(request, 'update_package.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
	




def customer_packageoptions(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_packageoptions = PackageOptions.objects.get(id=pk)
		return render(request, 'packageoption.html', {'customer_packageoptions':customer_packageoptions})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')
	
def delete_packageoptions(request, pk):
	if request.user.is_authenticated:
		delete_it = PackageOptions.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Package Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def add_packageoptions(request):
	form = AddPackageOptionForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_packageoptions = form.save()
				messages.success(request, "Package Added...")
				return redirect('home')
		return render(request, 'add_packageoption.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


def update_packageoptions(request, pk):
	if request.user.is_authenticated:
		current_packageoption = PackageOptions.objects.get(id=pk)
		form = AddPackageOptionForm(request.POST or None, instance=current_packageoption)
		if form.is_valid():
			form.save()
			messages.success(request, "Package Has Been Updated!")
			return redirect('home')
		return render(request, 'update_packageoption.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
	



def customer_subscription(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_subscription = Subscription.objects.get(id=pk)
		return render(request, 'subscription.html', {'customer_subscription':customer_subscription})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')
	
def delete_subscription(request, pk):
	if request.user.is_authenticated:
		delete_it = Subscription.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Subscription Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def add_subscription(request):
	form = AddSubscriptionForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_subscription = form.save()
				messages.success(request, "Subscription Added...")
				return redirect('home')
		return render(request, 'add_subscription.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


def update_subscription(request, pk):
	if request.user.is_authenticated:
		current_subscription = Subscription.objects.get(id=pk)
		form = AddSubscriptionForm(request.POST or None, instance=current_subscription)
		if form.is_valid():
			form.save()
			messages.success(request, "Subscription Has Been Updated!")
			return redirect('home')
		return render(request, 'update_subscription.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')