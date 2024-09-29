from django.views.generic import TemplateView


class IndexTemplate(TemplateView):
    template_name = 'main/index.html'
