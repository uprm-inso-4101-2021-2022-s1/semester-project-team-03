from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def usersettings(request):
    return render(request, 'settings/settings.html')