from django.views.generic import TemplateView

from main.services import get_all_mailings_len_from_cache, get_active_mailings_len_from_cache, \
    get_all_clients_len_from_cache, get_popular_blogs_from_cache


class IndexTemplate(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Главная'

        context_data['all_mailings_len'] = get_all_mailings_len_from_cache()
        context_data['active_mailings_len'] = get_active_mailings_len_from_cache()
        context_data['all_clients_len'] = get_all_clients_len_from_cache()
        context_data['popular_blogs'] = get_popular_blogs_from_cache()
        return context_data
