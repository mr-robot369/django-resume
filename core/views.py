from django.shortcuts import render
from .utils import *
from .forms import ContactForm

# Create your views here.
def home(request):
    context={'home':'active'}
    return render(request, "core/home.html",context)

def contact(request):
    form = ContactForm(request.POST or None)
    # print("hello")
    if form.is_valid():
        print("hello34")
        # Extract data from the form
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject=form.cleaned_data['subject']
        message = form.cleaned_data['message']
        # print(name,email,subject,message)
        body=f'''{name} having mail {email} sends you a message:
        {message}
        '''
        data={
            'subject':f'Contact : {subject}',
            'body': body,
        }
        Util.send_email(data)
    else:
        print(form.errors)
    context={'contact':'active','form':form}
    return render(request, "core/contact.html",context)