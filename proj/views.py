from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.shortcuts import render
from .DataCollector import getReviews

from .forms import NameForm
def current_datetime(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            rlist = getReviews(form.cleaned_data['search_query'])
            return render(request, 'index.html', {'form': form,
                                                  'data': form.cleaned_data['search_query'],
                                                  'reviews': rlist})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'index.html', {'form': form})