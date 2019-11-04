from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,
CreateView,UpdateView,DeleteView)
# Create your views here.
from . models import Group
from django.utils import timezone
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin

class GroupList(ListView):
    model = Group
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class GroupCreate(LoginRequiredMixin,CreateView):
    model = Group
    fields = ['name','description']
    # this is the default form
    # form_class = GroupForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        print(f'user is {form.instance.user.username}')
        return super().form_valid(form)

class GroupViewDetails(DetailView):
    model = Group

class GroupListView(ListView):
    model = Group

class GroupUpdate(UpdateView):
    pass
class GroupDelete(DeleteView):
    model = Group

class JoinGroup(TemplateView):
    pass
class LeaveGroup(TemplateView):
    pass
