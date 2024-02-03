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
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'
    ordering = ['-time_create']
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.filter(is_published=True)
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
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['latest_post'] = Post.objects.filter(is_published=True).order_by('-time_create')[:5]
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        queryset = Post.objects.filter(is_published=True)
        filter = PostFilter(self.request.GET, queryset=queryset)
        return filter.qs

    def get_object(self, queryset=None):
        # Получение объекта поста по первичному ключу
        return get_object_or_404(Post, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['latest_comments'] = Comment.objects.filter(post=self.object, is_published=True).order_by('-time_create')[:50]

        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['latest_post'] = Post.objects.filter(is_published=True).order_by('-time_create')[:5]

        # try:
        #     # Получите предыдущую и следующую новости
        #     previous_post = Post.objects.filter(
        #         time_create__lt=self.object.time_create, is_published=True
        #     ).order_by('-time_create').first()
        #
        #     next_post = Post.objects.filter(
        #         time_create__gt=self.object.time_create, is_published=True
        #     ).order_by('time_create').first()
        #
        #     context['previous_post'] = previous_post
        #     context['next_post'] = next_post
        # except Post.DoesNotExist:
        #     # Объект не найден - установим None для предыдущей и следующей новости
        #     context['previous_post'] = None
        #     context['next_post'] = None

        return context


class CategoryListView(ListView):
    model = Category
    template_name = 'blog/category_list.html'
    context_object_name = 'categories'


class CategoryPostsView(ListView):
    model = Post
    template_name = 'blog/category_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Post.objects.filter(categories=category, is_published=True).order_by('-time_create')


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post_detail', args=[self.kwargs['pk']])


class LikeCreateView(CreateView):
    model = Like
    fields = ['post', 'user']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddPostView(View):
    template_name = 'blog/add_post.html'  # Создайте шаблон add_post.html

    def get(self, request):
        form = PostForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Предполагается, что у вас есть система пользователей
            post.save()
            return redirect('blog:post_detail', pk=post.pk)  # Замените на ваш URL для просмотра поста
        return render(request, self.template_name, {'form': form})