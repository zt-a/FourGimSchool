from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Gallery


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super(GalleryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form'  # Поменяйте на класс, который используется в ваших стилях
        self.helper.layout = Layout(
            Submit('submit', 'Добавить', css_class='generic-btn success large')
        )

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'single-input'  # Добавьте классы, которые вам нужны для каждого поля

    def clean(self):
        cleaned_data = super(GalleryForm, self).clean()

        for field_name, field_errors in self.errors.items():
            for error in field_errors:
                self.fields[field_name].widget.attrs['class'] = 'form-control is-invalid text-danger'
                break

        return cleaned_data
