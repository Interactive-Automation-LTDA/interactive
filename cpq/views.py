from django.shortcuts import render

# Create your views here.
def manufacture_list(request):
    return render(request, 'cpq/manufacture_list.html')