from django.shortcuts import render

# Create your views here.
# bronken_access_control
def security_miscounfiguration(request):
    return render(request, 'security_miscounfiguration/index.html')
