from django.shortcuts import render
from django.template import loader
from .db import get_display_options
import json



def i_form(request):
    template = loader.get_template('index.html')
    data=get_display_options()
    input=request.POST
    insert_ip(input)


    return render(request, 'index.html', {'data':data}) 

def insert_ip(input):
    print(input)
    

