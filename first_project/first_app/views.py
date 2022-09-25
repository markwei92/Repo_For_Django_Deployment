from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from first_app.models import Accessrecord,Topic,Webpage,User,UserProfileInfo
from first_app import forms
from first_app.forms import FormName,NewUserForm,UserProfileInfoForm,UserForm 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# from first_project import first_app
# Create your views here.

#Lvl One & Two
def index(request):
    webpages_list = Accessrecord.objects.order_by('date')
    my_dict = {'access_records':webpages_list}
    # my_dict = {'insert_me': "Hello I am from views.py"}
    return render(request, 'first_app/index.html', context=my_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    
    registered = False
    
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                
            profile.save()
            
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else: 
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        
    return render(request, 'first_app/registration.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})    

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account Not Active')
        else:
            print('login failed')
            return HttpResponse('Invalid login details')
    else:
        return render(request, 'first_app/login.html')
                
#Lvl Three
# def index(request):
#     return render(request, 'first_app/index.html') 

# def form_name_view(request):
#     form = forms.FormName()
    
#     if request.method == 'POST':
#         form = forms.FormName(request.POST)
        
#         if form.is_valid():
#             #Do Something
#             print('Success!')
#             print(form.cleaned_data['name'])
#             print(form.cleaned_data['email'])
#             print(form.cleaned_data['text'])
            
#     return render(request,'first_app/form_page.html', {'form':form})

def users(request):
    
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    
    form = NewUserForm()
    
    if request.method == "POST":
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Invalid Form')
            
    return render(request, 'first_app/form_page.html', {'form': form}) 

def other(request):
    return render(request, 'first_app/other.html')

def relative(request):
    context_dict = {'text':'hello world','number':100}
    return render(request, 'first_app/relative_url_template.html',context_dict)
    