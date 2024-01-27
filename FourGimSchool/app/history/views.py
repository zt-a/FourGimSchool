from django.shortcuts import render
from django.views import View

from .models import History


# Create your views here.
class HistoryListView(View):
    template_name = 'history/history.html'

    def get(self, request):
        # Получение всех объектов History из базы данных
        histories = History.objects.all()

        # Передача списка историй в шаблон для отображения
        return render(request, self.template_name, {'histories': histories})


class HistoryDetailView(View):
    template_name = 'history/detail_history.html'

    def get(self, request, history_id):
        history = History.objects.get(id=history_id)
        return render(request, self.template_name, {'history': history})
