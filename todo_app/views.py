from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils import timezone
from .models import Todo

import json


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    title = "Home"
    extra_context = {'title': title}
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_now'] = timezone.now()
        todos_sample = ['this', 'and this']
        context['todos'] = json.dumps(todos_sample)
        return context
