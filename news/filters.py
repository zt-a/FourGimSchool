import django_filters
from .models import News

class NewsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Заголовок')

    class Meta:
        model = News
        fields = ['title']
