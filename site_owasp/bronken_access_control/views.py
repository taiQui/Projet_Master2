from django.shortcuts import render

# Create your views here.
# bronken_access_control
def bronken_access_control(request):
    return render(request, 'bronken_access_control/index.html')
