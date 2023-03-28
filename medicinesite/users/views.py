from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# crud
from .models import RegisterForm
from .forms import MyRegisterForm
from django.views.decorators.csrf import csrf_protect

# login&logout
def home(request):
    return render(request,'users/home.html')

# crud home
@login_required()
def home(request):
    data=RegisterForm.objects.all()
    if(data!=''):
        return render(request, 'users/home.html',{'data':data})
    else:
        return render(request, 'users/home.html')

# insert
@csrf_protect
def insert(request):
    if request.method=='POST':
        form= MyRegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,"Registration Successfully Completed")
                return redirect("Home")
            except:
                pass
    else:
        form= MyRegisterForm()       
    return render(request,"users/register.html",{'form':form})

# userregistration
def userregisteration(request):
    return render(request, 'users/userregisteration.html')


# its for login register
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect("Home")
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

# update
@csrf_protect
def update(request,id):
    data=RegisterForm.objects.get(id=id)
    if request.method=='POST':
        location=request.POST['location']
        medicinename=request.POST['medicinename']
        medicinecategory=request.POST['medicinecategory']
        symptoms=request.POST['symptoms']
        
        data.location=location
        data.medicinename=medicinename
        data.medicinecategory=medicinecategory
        data.symptoms=symptoms
        data.save()
        messages.success(request,"Update Successfully Completed")
        return redirect("Home")
    return render(request,"users/update.html",{'data':data})




# delete
def  delete(request,id):
    data=RegisterForm.objects.get(id=id)
    data.delete()
    messages.error(request,"Delete Sucessfully Completed")
    return redirect('Home')



# for profile
@login_required()
def profile(request):
    return render(request, 'users/profile.html')

# about
@login_required()
def about(request):
    return render(request,'users/about.html')

# contact
@login_required()
def contact(request):
    return render(request,'users/contact.html')

