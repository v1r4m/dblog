from django.shortcuts import render
from .models import Template, TextField, SelectField, Selection
from django.utils import timezone

# Create your views here.
def template_list(request):
    templates = Template.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'kokoo/template_list.html', {'templates':templates})
