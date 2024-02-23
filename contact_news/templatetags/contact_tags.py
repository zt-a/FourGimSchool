from django import template
from contact_news.forms import ContactForm, ContactFormPlus

register = template.Library()


@register.inclusion_tag("contact_news/tags/form.html")
def contact_form(layout=False):
    if not layout:
        return {'contact_form': ContactForm(), 'layout': layout}
    return {'contact_form': ContactFormPlus(), 'layout': layout}
