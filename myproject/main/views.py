from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello, Jitesh! Your Django app is running.</h1>")

def add_numbers(request):
    a = 10
    b = 20
    result = a + b
    return HttpResponse(f"Addition Result: {result}")

def php_style(request):
    name = "Jitesh"
    age = 20
    return HttpResponse(f"""
        <h2>User Details</h2>
        <p>Name: {name}</p>
        <p>Age: {age}</p>
    """)
def college(request):
    name = "Parul University"
    Sess = "2024-2028"
    Location = "Vadodara , Gujarat", 391760
    return HttpResponse(f"""
        <div style="text-align: center; margin-top: 50px; font-family: Arial, sans-serif;">
            <h2>User's College Details</h2>
            <hr>
            <h1>Name: {name}</h1>
            <p>Session: {Sess}</p>
            <p>location: {Location}</p>
        </div>
    """)
    def fee_check(request):
        return render(request,'course/fees.html',{
            'fees': 74500
        })
def courseview(request):
            return render(request, 'html/courseview.html', {'fees': 3500})