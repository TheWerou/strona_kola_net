from django.views.generic import TemplateView, DetailView, View
from django.shortcuts import redirect, HttpResponseRedirect, render
from .models import UserNet
from . logic import Logic
from .forms import EmailForm


class IndexView(TemplateView):
    template_name = "index.html"

    def __init__(self):
        super().__init__()
        self.logic_object = Logic()

    def get(self, request, *args, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['users'] = self.logic_object.get_rest()
        context['boss'] = self.logic_object.get_boss()

        if request.method == 'GET':
            context['email'] = EmailForm(self.request.GET)

            if context['email'].is_valid():
                context['email'].save()

                return redirect('/')

        return render(request, self.template_name , context)


class PersolnalView(DetailView):
    template_name = "osoba.html"
    model = UserNet


index_view = IndexView.as_view()
personal_view = PersolnalView.as_view()

