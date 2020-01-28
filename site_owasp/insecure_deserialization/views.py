from django.shortcuts import render

# Create your views here.
# bronken_access_control
def insecure_deserialization(request):
    return render(request, 'insecure_deserialization/index.html')
