from django.shortcuts import render
from .models import Todo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IndexListView(ListView):
    model = Todo
    context_objects_name = 'todo_list'
    template_name = 'index.html'

class TodoCreateView(LoginRequiredMixin,CreateView):
    model = Todo
    fields = ['title','date','text']
    context_objects_name = 'form'
    template_name = 'text.html'
    success_url = reverse_lazy('index')

class TodoUpdateView(LoginRequiredMixin,UpdateView):
    model = Todo
    fields = ['date','text']
    template_name = 'edit.html'
    context_objects_name = 'form'
    success_url = reverse_lazy('index')

class TodoDeleteView(LoginRequiredMixin,DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('index')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your Account is NOT active")
        else:
            return HttpResponse('INVALID LOGIN REQUIRED')
    else:
        return render(request, 'login.html', {})
# def index(request):
#     return render(request, 'index.html')
#
# def delete(request):
#     return render(request, 'delete.html')
#
# def edit(request):
#     return render(request, 'edit.html')
