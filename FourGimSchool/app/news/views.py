from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News
from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Comment
from .forms import CommentForm
from accounts.models import CustomUser


class NewsListView(ListView):
    model = News
    template_name = 'news/news.html'
    context_object_name = 'news_list'


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    slug_field = 'slug'
    pk_url_kwarg = 'pk'
    # context_object_name = 'detail_post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # news = get_object_or_404(News)
        context['comment_form'] = CommentForm()
        context['latest_comments'] = Comment.objects.filter(news=self.object).order_by('-time_create')[:50]

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
