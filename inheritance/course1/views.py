from django.shortcuts import render

# Create your views here.

  
def course1_page(request):
    return render(request, 'course1/course1.html')