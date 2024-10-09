from django.views.generic import TemplateView

from blog.models import Blog
from mailings.models import Mailing, Client


class IndexTemplate(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Главная'

        all_mailings = Mailing.objects.all()
        all_clients = Client.objects.all()

        context_data['all_mailings_len'] = len(all_mailings)
        context_data['active_mailings_len'] = len(all_mailings.exclude(status='off'))
        context_data['all_clients_len'] = len(all_clients)
        context_data['popular_blogs'] = Blog.objects.order_by('-views_count')[:3]
        return context_data
