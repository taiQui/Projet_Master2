from django.shortcuts import render

# Create your views here.
# bronken_access_control
def sensitive_data_exposure(request):
    return render(request, 'sensitive_data_exposure/index.html')
