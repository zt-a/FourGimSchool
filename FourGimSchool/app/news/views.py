from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News
from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Comment
from .forms import CommentForm
from accounts.models import CustomUser
from .filters import NewsFilter


class NewsListView(ListView):
    model = News
    template_name = 'news/news.html'
    context_object_name = 'news_list'
    paginate_by = 10  # Количество новостей на одной странице

    def get_queryset(self):
        queryset = News.objects.all()
        filter = NewsFilter(self.request.GET, queryset=queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news_list = context['news_list']

        paginator = Paginator(news_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            news = paginator.page(page)
        except PageNotAnInteger:
            # Если номер страницы не является целым числом, возвращаем первую страницу
            news = paginator.page(1)
        except EmptyPage:
            # Если номер страницы больше максимального, возвращаем последнюю страницу
            news = paginator.page(paginator.num_pages)



        context['news_list'] = news
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        context['latest_news'] = News.objects.filter(is_published=True).order_by('-time_create')[:5]
        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    slug_field = 'slug'
    pk_url_kwarg = 'pk'
    # context_object_name = 'detail_post'

    def get_queryset(self):
        queryset = News.objects.all()
        filter = NewsFilter(self.request.GET, queryset=queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # news = get_object_or_404(News)
        context['comment_form'] = CommentForm()
        context['latest_comments'] = Comment.objects.filter(news=self.object).order_by('-time_create')[:50]

        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        context['latest_news'] = News.objects.filter(is_published=True).order_by('-time_create')[:5]

        # Получите предыдущую и следующую новости
        context['previous_news'] = News.objects.filter(
            time_create__lt=self.object.time_create, is_published=True
        ).order_by('-time_create').first()

        context['next_news'] = News.objects.filter(
            time_create__gt=self.object.time_create, is_published=True
        ).order_by('time_create').first()

        return context


def add_comment(request, slug):
    news = get_object_or_404(News, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.author = request.user
            comment.save()
            return redirect('news:news_detail', slug=slug)
    else:
        form = CommentForm()

    context = {
        'form': form,
        'news': news,
   }

    return render(request, 'news/add_comment.html', context=context)
