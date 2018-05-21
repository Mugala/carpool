from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome(request):
    return render (request, "rwelcome.html")

def search_results(request):

    if 'destination' in request.GET and request.GET["destination"]:
        search_term = request.GET.get("destination")
        searched_destinations = Driver.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'dtemp/search.html',{"message":message,"destinations": searched_destinations})

    else:
        message = "You haven't searched for any term"
        return render(request, 'dtemp/search.html',{"message":message})