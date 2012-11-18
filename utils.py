from django.template import RequestContext
from django.shortcuts import render

def response(request, template, params):
    return render(request, template, params, context_instance=RequestContext(request))
