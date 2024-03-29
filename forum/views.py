from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Category, Comment, Like
from .forms import CommentForm, PostForm
from .filters import *


class PostListView(ListView):
    model = Post
    template_name = 'forum/post_list.html'
    context_object_name = 'post_list'
    ordering = ['-time_create']
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.only('time_create', 'title', 'content', 'author', 'pk').filter(is_published=True).select_related('author')
        filter = PostFilter(self.request.GET, queryset=queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_list = context['post_list']

        paginator = Paginator(post_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # Если номер страницы не является целым числом, возвращаем первую страницу
            posts = paginator.page(1)
        except EmptyPage:
            # Если номер страницы больше максимального, возвращаем последнюю страницу
            posts = paginator.page(paginator.num_pages)

        context['post_list'] = posts
        context['title'] = f'Форум'
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['latest_post'] = Post.objects.filter(is_published=True).order_by('-time_create')[:5]
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'forum/post_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        queryset = Post.objects.filter(is_published=True)
        filter = PostFilter(self.request.GET, queryset=queryset)
        return filter.qs

    def get_object(self, queryset=None):
        # Получение объекта поста по первичному ключу
        return get_object_or_404(Post, pk=self.kwargs['pk'], is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['latest_comments'] = Comment.objects.filter(post=self.object).order_by('-time_create')[:50]
        context['title'] = f'{self.get_object().title}'

        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['latest_post'] = Post.objects.filter(is_published=True).order_by('-time_create')[:5]

        return context


class CategoryListView(ListView):
    model = Category
    template_name = 'forum/category_list.html'
    context_object_name = 'categories'


class CategoryPostsView(ListView):
    model = Post
    template_name = 'forum/category_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'], is_published=True)
        return Post.objects.filter(categories=category).order_by('-time_create')


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'forum/comment_form.html'

    def form_valid(self, form):
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'], is_published=True)
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('forum:post_detail', args=[self.kwargs['pk']], is_published=True)


class LikeCreateView(CreateView):
    model = Like
    fields = ['post', 'user']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddPostView(View):
    template_name = 'forum/add_post.html'  # Создайте шаблон add_post.html

    def get(self, request):
        form = PostForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Предполагается, что у вас есть система пользователей
            post.save()
            return redirect('forum:post_detail', pk=post.pk)  # Замените на ваш URL для просмотра поста
        return render(request, self.template_name, { 'form': form, 'title': 'Добавление поста' })