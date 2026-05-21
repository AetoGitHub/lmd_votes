from django.views import generic as g
from django.urls import reverse_lazy
from .forms import MensajeForm
from .models import Mensaje


class Home(g.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class MensajeCreateView(g.edit.CreateView):
    model = Mensaje
    form_class = MensajeForm
    template_name = 'test/mensaje_form.html'
    success_url = reverse_lazy('mensaje_lista')


class MensajeListView(g.ListView):
    model = Mensaje
    template_name = 'test/mensaje_lista.html'
    context_object_name = 'mensajes'