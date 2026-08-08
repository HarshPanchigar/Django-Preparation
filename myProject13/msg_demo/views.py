from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def show_msg(request):
    messages.debug(request, 'this is debug a message.')
    messages.info(request,'this is a info message')
    messages.warning(request,'this is a warning message')
    messages.success(request,'this is a success message')
    messages.error(request,'this is a error message')

    return render(request,'show_msg.html')