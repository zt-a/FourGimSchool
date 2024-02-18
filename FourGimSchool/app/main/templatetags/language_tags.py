from django import template
from django.utils.translation import get_language_info
from django.conf import settings

register = template.Library()


@register.inclusion_tag('language_dropdown.html')
def language_dropdown():
    languages = [(lang_code, get_language_info(lang_code)['name_local']) for lang_code, _ in settings.LANGUAGES]

    return {'LANGUAGES': languages}
