from django.shortcuts import render
from django.views.generic import TemplateView

class ScholarDashboardView(TemplateView):
    template_name = 'scholar/home.html'

class ScholarProfileView(TemplateView):
    template_name = 'scholar/scholar_profile.html'