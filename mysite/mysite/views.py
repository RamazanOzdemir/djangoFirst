from django.http import HttpResponse
from django.shortcuts import render

def about(request):
   # return HttpResponse('about page')
   return render(request,'about.html')
def homepage(request):
   # return HttpResponse('homepage page')
   return render(request,'homepage.html')