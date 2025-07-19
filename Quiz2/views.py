from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DetailView, DeleteView
from django.urls import reverse_lazy

def portfolio(request):
    return render(request, 'portfolio/base.html')

def applicant_list(request):
    applicants = User.objects.filter(portfolio__isnull=False).order_by('first_name')
    context = {
        'applicants': applicants,
        'position': 'Junior Developer'  # Hardcoded position
    }
    return render(request, 'portfolio/applicant_list.html', context)