from django import forms
from .models import Comment, Like, Post, Category


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='Введите сообщение', widget=forms.Textarea(attrs={
        'class': 'form-control w100',
        'placeholder': 'Введите комментарий',
        'name': 'message',
        'id': 'message',
        'cols': '30',
        'rows': '9',
        'onfocus': "this.placeholder = ''",
        'onblur': "this.placeholder = 'Введите сообщение'"
    }))

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control w100',
                'placeholder': 'Введите комментарий',
                'name': 'content',
                'id': 'content',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Введите сообщение'"
            }),
        }


class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ['post', 'user']

    def save(self, commit=True):
        # Убедитесь, что user не добавляется вручную, если вы используете автоматическое присвоение в представлении.
        like = super().save(commit=False)
        if commit:
            like.save()
        return like


class PostForm(forms.ModelForm):
    categories = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={
        'class': 'form-select single-input'
    }))

    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control w100',
                'placeholder': 'Введите текст',
                'name': 'content',
                'id': 'content',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Введите текст'"
            }),
            'title': forms.TextInput(attrs={

                'class': 'form-control w100',
                'placeholder': 'Введите текст',
                'name': 'title',
                'id': 'title',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Введите текст'"
            }),
        }
