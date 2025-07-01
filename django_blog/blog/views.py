from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(published=True).order_by('-created_at')

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return Post.objects.filter(published=True)

class CategoryPostListView(ListView):
    model = Post
    template_name = "blog/category_post_list.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        category_slug = self.kwargs.get('slug')
        category = get_object_or_404(Category, slug=category_slug)
        return Post.objects.filter(published=True, categories=category).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return context

class TagPostListView(ListView):
    model = Post
    template_name = "blog/tag_post_list.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        tag_slug = self.kwargs.get('slug')
        tag = get_object_or_404(Tag, slug=tag_slug)
        return Post.objects.filter(published=True, tags=tag).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = get_object_or_404(Tag, slug=self.kwargs.get('slug'))
        return context
