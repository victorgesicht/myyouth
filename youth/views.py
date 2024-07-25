from django.shortcuts import render
from youth.models import general_info

# Create your views here.

def home(request):
    context={
        "location": general_info.location,
        "phone":general_info.phone,
        "email":general_info.email,
        "open_hours":general_info.open_hours,
        "web_app_name":general_info.web_app_name
    }
    return render(request, 'index.html', {"context":context})


def about(request):
    return render(request, 'about.html', {})

