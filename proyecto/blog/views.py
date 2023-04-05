from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



def about (request):
    return render(request, "blog/about.html") 

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-pots_date'] 

class PostDetailView (LoginRequiredMixin, DetailView):

    model = Post

class PostCreateView (LoginRequiredMixin, CreateView):

    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):

        form.instance.author =self.request.user
        return super().form_valid(form)
    
    
    def test_func(self):
        post = self.get_object()
        
        if self.request.user == post.author:
            return True
        return False
    
class PostUpdateview (LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):

        form.instance.author =self.request.user
        return super().form_valid(form) 

    def test_func(self):
        post = self.get_object()
        
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(DeleteView):

    model = Post
    success_url = '/'


    def test_func(self):
        post = self.get_object()
        
        if self.request.user == post.author:
            return True
        return False