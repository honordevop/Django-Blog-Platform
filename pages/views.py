from django.shortcuts import render
from django.views.generic import ListView
from articles.models import Article
from django.urls import reverse_lazy
# Create your views here.


class HomePageView(ListView):
    model = Article
    template_name = 'home.html'
    success_url = reverse_lazy('home')
