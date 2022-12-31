from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from loginn.forms import loginform,signupform
from django.contrib.auth import authenticate,login,logout
from my.models import user_data
from PIL import Image, ImageOps
global email

def home(request):
    fm=loginform()

    if request.method=="POST":
        global email
        fm=loginform(request.POST)
        if fm.is_valid():
            email = fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            username=User.objects.get(email=email)
            user=authenticate(username=username.username,password=password)

            if User.objects.filter(email=email).exists():
                login(request, user)
                return redirect("/afterlogin")


                

    return render(request,"home.html",{"form":fm})

def signup(request):
    fm=signupform()
    if request.method=="POST":
        fm=signupform(request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']

            new_user=User.objects.create_user(username,email,password).save()
            return redirect("/")

    return render(request,"signup.html",{"form":fm})

def afterlogin(request):
    ob=user_data.objects.all()
    # for i in ob:


    if request.method=="POST":
        name=request.POST.get("name")
        age=request.POST.get("age")
        image=request.FILES.get("image")
        data=user_data(name=name,age=age,image=image,image1=image,image2=image,image3=image)
        data.save()

        return redirect("/afterlogin")

    return render(request,"afterlogin.html",{"ob":ob})

def save(self):

    img = Image.open(self.image.path)

    if img.height > 300 or img.width > 300:
        new_img = (200, 300)
        img.thumbnail(new_img)
        img.save(self.image.path)
    
    img = Image.open(self.image1.path)

    if img != None:
        new_img = (500, 500)
        img.thumbnail(new_img)
        img.save(self.image1.path)
    
    img = Image.open(self.image2.path)

    if img!=None:
        new_img = (1024, 768)
        img.thumbnail(new_img)
        img.save(self.image2.path)
    
    img = Image.open(self.image3.path) 

    if img!=None:
        new_img = ImageOps.grayscale(img)
        #img.thumbnail(new_img)
        new_img.save(self.image3.path)


    

                
    