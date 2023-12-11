# from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomeView(TemplateView):
    template_name = 'testing/home.html'


class AboutView(TemplateView):
    template_name = 'testing/about.html'
