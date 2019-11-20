from django.views.generic import TemplateView, DetailView
from django.shortcuts import redirect, render
from .models import UserNet
from . logic import Logic
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings


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
                subject = request.GET.get('temat')
                text = request.GET.get('tekst')
                email = request.GET.get('email')

                send_mail(subject=subject, message=text, from_email=settings.EMAIL_HOST_USER,
                          recipient_list=['sosape5375@4xmail.net'], fail_silently=False)

                return redirect('/')

        return render(request, self.template_name , context)


class PersolnalView(DetailView):
    template_name = "osoba.html"
    model = UserNet



index_view = IndexView.as_view()
personal_view = PersolnalView.as_view()

