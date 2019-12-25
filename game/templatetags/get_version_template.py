from django import template
from game.version import getVersion

register = template.Library()

@register.simple_tag
def get_version():
  return getVersion()