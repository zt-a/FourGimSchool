from django.shortcuts import render
from django.views import View

from .models import History


# Create your views here.
class HistoryListView(View):
    template_name = 'history/history.html'

    def get(self, request):
        # Получение всех объектов History из базы данных
        histories = History.objects.filter(is_published=True)

        # Передача списка историй в шаблон для отображения
        return render(request, self.template_name, {'histories': histories, 'title': 'Истории'})


class HistoryDetailView(View):
    template_name = 'history/detail_history.html'

    def get(self, request, history_id):
        history = History.objects.get(id=history_id, is_published=True)
        return render(request, self.template_name, {'history': history, 'title': f'{history.title}'})
