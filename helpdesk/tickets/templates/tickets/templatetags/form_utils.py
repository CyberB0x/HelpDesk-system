from django import template
from django.utils.html import format_html

register = template.Library()

# Фильтр: добавляет CSS-класс полю формы
@register.filter(name='add_class')
def add_class(field, css):
    return field.as_widget(attrs={"class": css})

# Пример тега (если был в form_tags)
@register.simple_tag
def example_tag():
    return "Пример тега"
