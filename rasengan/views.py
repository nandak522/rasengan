from django.shortcuts import render_to_response

def home(request, home_template):
    return render_to_response(home_template)
