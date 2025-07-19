from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Portfolio, Project
from django.views.generic import DetailView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render

# Create your views here.
def applicant_list(request):
    applicants = User.objects.filter(portfolio__isnull=False).order_by('first_name')
    context = {
        'applicants': applicants,
        'position': 'Junior Developer' # Hardcoded position
    }
    return render(request, 'portfolio/applicant_list.html', context)

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/portfolio_detail.html'
    context_object_name = 'portfolio'

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username)
        return get_object_or_404(Portfolio, user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['applicant_user'] = self.object.user
        return context

class ApplicantDeleteView(DeleteView):
    model = User
    template_name = 'portfolio/applicant_confirm_delete.html'
    success_url = reverse_lazy('portfolio:applicant_list')

    def get_object(self, queryset=None):
        # Override get_object to fetch by username
        username = self.kwargs.get('username')
        return get_object_or_404(User, username=username)

    def form_valid(self, form):
        response = super().form_valid(form)
        return response