from django.shortcuts import render
from .models import Finch

# finches = [
# {'name': 'Lolo', 'breed': 'European Golfish', 'description': 'finches finches', 'age': 3},
# {'name': 'Sachi', 'breed': 'Brambling', 'description': 'finches finches', 'age': 2},
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

# Define the about view
def about(request):
    return render(request, 'about.html')

def finches_index(request):
    # Handles the request, points to the template to render, and we are providing a dict with a cats key which has a value of all the cats
    return render(request, 'finches/index.html', { 'finches': finches })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch})