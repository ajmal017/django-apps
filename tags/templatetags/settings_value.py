#*========================================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	Pull settings from settings.py
#*  Usage:		{% settings_value "LANGUAGE_CODE" %}
#*========================================== #
from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")

    