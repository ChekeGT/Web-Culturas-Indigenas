from django import forms
from .models import Culture


class CultureForm(forms.ModelForm):

    class Meta:
        model = Culture
        fields = ['name', 'image', 'image_description', 'description']
        widgets = {
            'name':forms.TextInput(attrs={
                'placeholder':'Introduce el nombre:',
                'class':'form-control mt-1 mb-2',

            }),
            'image_description':forms.TextInput(
                attrs={
                    'placeholder': 'Introduce una descripcion para la imagen:',
                    'class': 'form-control mb-2'
                }
            ),
            'description':forms.Textarea(
                attrs={
                    'placeholder':'Introduce una descripcion para la cultura',
                    'class':'form-control'
                }
            )
        }