from django.shortcuts import render

# Create your views here.
# bronken_access_control
def xml_external_entities(request):
    return render(request, 'xml_external_entities/index.html')
