from django.views.generic import ListView, DetailView
from  .models import Culture
from django.http.response import JsonResponse
# Create your views here.


class CultureListView(ListView):
    template_name = 'indigenous_culture/culture_list.html'
    model = Culture


class CultureDetailView(DetailView):
    template_name = 'indigenous_culture/culture_detail.html'
    model = Culture


class DictDetailView(DetailView):
    template_name = 'indigenous_culture/dict.html'
    model = Culture


def DictResponse(request, pk):
    json_response = {'answer':''}
    culture = Culture.objects.get(pk=pk)
    culture_words = [word.word_translated for word in culture.dict.words.all()]
    content = request.GET.get('content')
    if content:
        if content in culture_words:
            word = culture.dict.words.get(word_translated=content)
            json_response['answer'] = word.word
        else:
            json_response['answer'] = 'Palabra sin traduccion o inexistente'
    return  JsonResponse(json_response)