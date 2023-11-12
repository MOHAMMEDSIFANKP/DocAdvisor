from django.shortcuts import render

# Create your views here.

def Homepage(request):
    return render(request,'Homepage.html')

def review_entry(request):
    return render(request,'review_frorm.html')