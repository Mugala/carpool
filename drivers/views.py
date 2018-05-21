from django.shortcuts import render
from django.http import  HttpResponse,Http404,HttpResponseRedirect
from .models import Car,Pickup_location,Driver,NewsLetterRecipients
from .forms import NewsLetterForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required(login_url='/accounts/login/')
def welcome(request):
    details = Driver.driver_details()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()

            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('dwelcome')
    else:
        form = NewsLetterForm()     
    return render (request, "dwelcome.html",{"details":details, "letterForm":form})


def search_results(request):

    if 'destination' in request.GET and request.GET["destination"]:
        search_term = request.GET.get("destination")
        searched_destinations = Driver.search_by_destination(search_term)
        results = [*searched_destinations]
        message = f"{search_term}"

        return render(request, 'dtemp/search.html',{"message":message,"destinations": results})

    else:
        message = "You haven't searched for any term"
        return render(request, 'dtemp/search.html',{"message":message})


