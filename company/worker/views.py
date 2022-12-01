from django.shortcuts import render
from django.views.generic.base import View
from .models import Rabotnik, Departament
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView

class BlogListView(View):
    model = Rabotnik
    template_name = 'index.html'
    def get(self, request):
        posts = Rabotnik.objects.all()
        return render(request, 'index.html', {'post_list': posts})


class BlogDetailView(DetailView):  # new
    model = Rabotnik
    template_name = 'p_detail.html'


class BlogCreateView(CreateView):  # новое изменение
    model = Rabotnik
    template_name = 'p_new.html'
    fields = ['name', 'post', 'salary', 'departament']


class BlogUpdateView(UpdateView):  # Новый изм
    model = Rabotnik
    template_name = 'p_edit.html'
    fields = ['name', 'post']


class BlogDeleteView(DeleteView):  # Нов
    model = Rabotnik
    template_name = 'p_delete.html'
    success_url = reverse_lazy('index')