from django.urls import path
from .views import HomeView, CountryAboutView, CountryDealView, CountryReservationView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/<slug:slug>/', CountryAboutView.as_view(), name='about'),  
    path('deals/', CountryDealView.as_view(), name='deals'),
    path('reservation/', CountryReservationView.as_view(), name='reservation'),
]