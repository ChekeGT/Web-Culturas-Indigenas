from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from  .models import Culture
from .forms import CultureForm
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.utils.decorators import method_decorator
# Create your views here.


@method_decorator(staff_member_required(), name='dispatch')
class CultureCreateView(CreateView):
    template_name = 'indigenous_culture/culture_create_or_edit.html'
    model = Culture
    form_class = CultureForm

    def get_success_url(self):
        return reverse_lazy('culture_detail', args=[self.object.pk, slugify(self.object.name)]) + '?created'


@method_decorator(staff_member_required(), name='dispatch')
class CultureEditView(UpdateView):
    template_name = 'indigenous_culture/culture_create_or_edit.html'
    model = Culture
    form_class = CultureForm

    def get_success_url(self):
        return reverse_lazy('culture_detail', args=[self.object.pk, slugify(self.object.name)]) + '?updated'


@method_decorator(staff_member_required(), name='dispatch')
class CultureDeleteView(DeleteView):
    template_name = 'indigenous_culture/culture_delete.html'
    model = Culture

    def get_success_url(self):
        return reverse_lazy('culture_list') + '?deleted'

class CultureListView(ListView):
    template_name = 'indigenous_culture/culture_list.html'
    model = Culture


class CultureDetailView(DetailView):
    template_name = 'indigenous_culture/culture_detail.html'
    model = Culture


