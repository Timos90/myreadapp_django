from django import template

# Singleton
# meaning, each time you add a filter, you need to restart the terminal
register = template.Library()

@register.filter
def semi_colon_seperator(value):
    return value.replace(', ', '; ')

@register.filter
def extract_tags_and_authors(values):
    return ', '.join(str(value) for value in values)
    