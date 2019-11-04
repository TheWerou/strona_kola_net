from django.views.generic import TemplateView
from .models import UserNet
from . logic import Logic


class IndexView(TemplateView):
    template_name = "index.html"

    def __init__(self):
        super().__init__()
        self.logic_object = Logic()

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['users'] = self.logic_object.get_sorted()
        return context


index_view = IndexView.as_view()
