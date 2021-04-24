from django.shortcuts import render

def render_main_page(request):
    return render(request,'main/main_page.html')

# Create your views here.
