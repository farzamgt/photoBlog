from django import template

register = template.Library()

@register.filter
def add_class(value, css_class):
    """Add a CSS class to form fields."""
    return value.as_widget(attrs={'class': css_class})
