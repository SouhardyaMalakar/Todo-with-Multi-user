from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
# Create your views here.
class TaskList(LoginRequiredMixin,ListView):
    model=Task
    context_object_name='tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks']= context['tasks'].filter(user=self.request.user)
        return context

    
class TaskDetail(LoginRequiredMixin,DetailView):
    model=Task
    context_object_name='task'
    template_name='base/task.html'

class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    fields = ['title', 'description', 'complete']
    #i donno wtf is diz shit
    success_url = reverse_lazy('tasks')   

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model=Task
    fields = ['title', 'description', 'complete' ]
    #i donno wtf is diz shit
    success_url = reverse_lazy('tasks')  
class TaskDelete(LoginRequiredMixin,DeleteView):
    model=Task
    #i donno wtf is diz shit
    success_url = reverse_lazy('tasks')
    template_name='base/delete.html'  

class CustomLoginView(LoginView):
    template_name='base/login.html'
    fields = '__all__'
    redirect_authenticated_user=True
    def get_success_url(self):
        return reverse_lazy('tasks')
