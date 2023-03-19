from django import template

register = template.Library()


@register.inclusion_tag('user_id_input.html')
def user_id(_id):
    return {'user_id': _id}
