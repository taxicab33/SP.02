from django import template


register = template.Library()

NABAR_LINKS = {
    'equipment': 'Оборудование',
    'expendable_materials': 'Расходные материалы',
    'users': 'Пользователи',
    'inventory': 'Инвентаризации'
}


@register.simple_tag
def navbar_links():
    return NABAR_LINKS
