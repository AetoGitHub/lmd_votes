from django.views import generic as g
from django.urls import reverse_lazy
from .forms import FeminosForm
from .models import Feminosa


class FeminosalistView(g.ListView):
    model = Feminosa
    template_name = 'draga/draga_list.html'
    context_object_name = 'dragas'


class FeminosacreateView(g.edit.CreateView):
    model = Feminosa
    form_class = FeminosForm
    template_name = 'draga/draga_create.html'
    success_url = reverse_lazy('draga_list')
