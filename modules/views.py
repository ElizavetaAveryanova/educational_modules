from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Контроллер просмотра домашней страницы"""
    template_name = 'modules/index.html'
