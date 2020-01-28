from django.shortcuts import render

# Create your views here.
# bronken_access_control
def xss(request):
    return render(request, 'xss/index.html')
