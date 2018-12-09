from django.http.response import JsonResponse, Http404
from .models import Word
from django import forms
from django.views.generic import  DetailView,DeleteView, UpdateView
from  indigenous_culture.models import Culture
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# Create your views here.
class DictDetailView(DetailView):
    template_name = 'translate/translate.html'
    model = Culture

@method_decorator(staff_member_required(), name='dispatch')
class WordListView(DetailView):
    template_name = 'translate/word_edit_or_delete.html'
    model = Culture

    def get_object(self, queryset=None):
        obj = super(WordListView, self).get_object()
        if len(obj.dict.words.all()) > 0:
            return obj
        else:
            raise Http404

@method_decorator(staff_member_required(), name='dispatch')
class WordsCreateView(DetailView):
    model = Culture
    template_name = 'translate/dict_add.html'

@method_decorator(staff_member_required(), name='dispatch')
class WordsDeleteView(DeleteView):
    model = Word
    template_name = 'translate/word_delete.html'

    def get_success_url(self):
        return reverse_lazy('culture_list') + '?word_deleted'


class WordEditView(UpdateView):
    model = Word
    template_name = 'translate/word_update.html'
    fields = ['word', 'word_translated']
    success_url = reverse_lazy('culture_list')

    def get_form(self, form_class=None):
        form = super(WordEditView, self).get_form()
        form.fields['word'].widget = forms.Textarea(attrs={
        'class':'form-control', 'placeholder':'Introduce la palabra en lengua indigena'})
        form.fields['word_translated'].widget = forms.Textarea(attrs={
            'class': 'form-control', 'placeholder': 'Introduce la palabra en espanol'})
        return form

@staff_member_required()
def WordEditOrDeleteResponse(request,pk):
    json_response = {'word_pk': False}
    try:
        culture = Culture.objects.get(pk=pk)
        print(request.GET.get('word'))
        word = culture.dict.words.get(word_translated=request.GET.get('word'))
        json_response['word_pk'] = word.pk
        print(json_response)
        return JsonResponse(json_response)
    except Word.DoesNotExist:
        print(json_response)
        return JsonResponse(json_response)
    except Exception as e:
        print(type(e).__name__)
@staff_member_required()
def DictEditResponse(request, pk):
    json_response = {'word': False, 'word_tranlated': False}
    'Obtenemos la cultura en base a su pk'
    culture = Culture.objects.get(pk=pk)
    'Obtenemos la palabra en la lengua indigena'
    word = request.GET.get('word')
    'Obtenemos la palabra en espanol'
    word_translated = request.GET.get('word_translated')
    'Si las palabras tanto en ingles como en espanol existen'
    if word and word_translated:
        'Intentamos'
        try:
            for word in culture.dict.words.all():
                if word.word_translated == word_translated:
                    raise ValueError
            '''Creamos un objeto de tipo palabra con la palabra en 
                lenguaje indigena y la palabra en espanol'''
            word_object = Word.objects.create(word=word, word_translated=word_translated)
            'Lo agregamos al diccionario'
            culture.dict.words.add(word_object)
        except Exception as e:
            'Si ocurre algun error imprimos el error'
            print(type(e).__name__)
        else:
            'Si todo sale bien agregamos true a los dos valores'
            json_response['word_tranlated'] = True
            json_response['word'] = True
        'Retornamos el JsonResponse'
    return JsonResponse(json_response)


def DictResponse(request, pk):
    json_response = {'answer':''}
    #Obtenemos La cultura mediante su pk
    culture = Culture.objects.get(pk=pk)
    #Obtenemos las palabras en espanol dentro de esa cultura
    culture_words = [word.word_translated for word in culture.dict.words.all()]
    content = request.GET.get('content')
    #Comprobamos si existe contenido
    if content:
        """Comprobamos si la palabra que se mando a
         traducir esta dentro del diccionario de la cultura"""
        if content in culture_words:
            #Obtenemos un queryset filtrando por la palbra en espanol
            words = culture.dict.words.filter(word_translated=content)
            if len(words) == 1:
                #Si  la longitud de el queryset es uno es facil, solo asiganmos el valor directamente
                words = culture.dict.words.get(word_translated=content)
                json_response['answer'] = words.word
            else:
                """De lo contrario tenemos que crear una lista
                con todas las palabras en esa lengua que coincidan
                que tengan como valor en espanol el mismo que envio
                el usuario y asignarlas dentro de un string para 
                mandarla en el JsonResponse"""
                words_list = [',{}'.format(word.word) for word in words]
                answer = ''
                for word in words_list:
                    answer += word
                json_response['answer'] = answer
        #Si el contenido no esta dentro de el diccionario de la cultura
        else:
            json_response['answer'] = 'Palabra sin traduccion o inexistente'
    #Retornamos el JsonResponse
    return  JsonResponse(json_response)