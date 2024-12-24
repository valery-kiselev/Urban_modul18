from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
def func_template(request):
    return render(request, 'func_template.html')

# class class_template(TemplateView):
#     template_name = 'class_template.html'

class ClasTempl(View):
    def get(self, request):
        return HttpResponse('"Это шаблон для классового представления"')