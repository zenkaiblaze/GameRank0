from django.shortcuts import render
def return_index(request):
    return render (request, 'html/index.html')
# Create your views here.
