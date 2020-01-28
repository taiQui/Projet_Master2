from django.shortcuts import render

# Create your views here.
# bronken_access_control
def insufficient_log(request):
    return render(request, 'insufficient_log/index.html')
