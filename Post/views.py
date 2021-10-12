from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Genre
from django.urls import reverse_lazy
from .forms import PostForm,UpdatePostForm

""" def home(requests):
    return  render(requests,'home.html',{}) """

class HomeView(ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name='home.html'

class PostDetailsView(DetailView):
    model=Post
    template_name='post_details.html'

class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name="add_post.html"
    #fields= '__all__'

class AddGenreView(CreateView):
    model=Genre
    
    template_name="add_genre.html"
    fields= '__all__'

class UpdatePostView(UpdateView):
    model=Post
    form_class=UpdatePostForm
    template_name='update_post.html'
    #fields=['title','content']

class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('home')
    