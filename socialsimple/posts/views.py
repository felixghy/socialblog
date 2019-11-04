#### posts.view ####
from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,
CreateView,UpdateView,DeleteView)
# Create your views here.
from . models import Post
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import PostForm
from django.urls import reverse_lazy

class ListPost(ListView):
    model = Post
    #default template post_list.html
    def get_queryset(self):
        return Post.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')

class PostDetail(DetailView):
    model = Post

class CreatePost(LoginRequiredMixin,CreateView):
    # login_url=
        redirect_field_name ='post_detail.html'
        model = Post
    # either use default post_form.html or set template name specify path
    #    template_name = 'posts/post_form.html'

        form_class = PostForm
        # success_url = reverse_lazy('listpost')

        def form_valid(self, form):

            form.instance.user = self.request.user
            return super().form_valid(form)
