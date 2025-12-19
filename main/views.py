from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Country


class HomeView(TemplateView):
    template_name = "main/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.filter(is_active=True)
        return context


class CountryAboutView(DetailView):
    model = Country
    template_name = "main/about.html"
    context_object_name = 'country'  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CountryDealView(ListView):
    model = Country
    template_name = "main/deals.html"
    context_object_name = 'countries'
    
    def get_queryset(self):
        return Country.objects.filter(is_active=True)


class CountryReservationView(TemplateView):
    template_name = "main/reservation.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.filter(is_active=True)
        return context