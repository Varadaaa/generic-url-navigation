from django.shortcuts import render

# Create your views here.

def adhiti(request):
    return render(request, 'adhiti.html')



def preethi(request):
    return render(request, 'preethi.html')


def vishnu(request):
    return render(request, 'vishnu.html')