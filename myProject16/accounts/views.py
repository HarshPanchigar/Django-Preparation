from django.shortcuts import render , redirect
from .forms import ProfileForm
from .models import Profile
from django.contrib import messages

def upload_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile picture uploaded successfully')
            return redirect('view_profile')
        else:
            messages.error(request,'Error uploading profile picture')
    else:
        form = ProfileForm()
        return render(request,'upload_profile.html', {'form':form})

def view_profile(request):
    profile = Profile.objects.all()
    return render(request,'view_profile.html',{'profiles': profile} )
