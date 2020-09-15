from django.shortcuts import render
from newapp.models import GoldModelForm

# Create your views here.
def home_view(request, *args, **kwargs):
    form = GoldModelForm(initial={
        'first_name': 'First Name', 'last_name' : "Last Name",
        'phone_number' : 'Phone Number', 'email' : 'Email', 'adress' : 'Adress',
         'apt' : "Apt #", 'city' : 'City', 'state' : 'State', 'zip' : 'ZIP', 'country': 'USA'})

    if request.method == "POST":
        form = GoldModelForm(request.POST)
        if form.is_valid():
            form.save()
            return thank_you_view(request)

    return render(request, 'form.html', {'form' : form})

def thank_you_view(request, *args, **kwargs):
    return render(request, 'thank_you.html', {})
