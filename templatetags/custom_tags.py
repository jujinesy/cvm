import os
from django import template
from django.conf import settings

register = template.Library()

class AssignNode(template.Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def render(self, context):
        context[self.name] = getattr(settings, self.value.resolve(context, True), "")
        return ''

@register.tag('get_settings_value')
def do_assign(parser, token):
    bits = token.split_contents()
    if len(bits) != 3:
        raise template.TemplateSyntaxError("'%s' tag takes two arguments" % bits[0])
    value = parser.compile_filter(bits[2])
    return AssignNode(bits[1], value)

# Your template:
# {% load custom_tags %}
#
# # Set Static_Local template variable:
# {% get_settings_value settings_debug "DEBUG" %}
#
# # Output settings_debug variable:
# {{ settings_debug }}
#
# # Use variable in if statement:
# {% if settings_debug == True %}
# ... do something ...
# {% else %}
# ... do other stuff ...
# {% endif %}

@register.assignment_tag
def do_image_filter(arg):
    if os.path.splitext(arg)[1] in ('.jpg', '.jpeg', '.png'):
        return True
    return  False
