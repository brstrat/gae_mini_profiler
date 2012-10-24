import logging
import os


try:
    import json
except ImportError:
    import simplejson as json

from django.template import Library
register = Library()

@register.simple_tag
def profiler_includes_request_id(request_id, show_immediately = False):
    if not request_id:
        return ""
    from google.appengine.ext.webapp import template
    path = os.path.join(os.path.dirname(__file__), "../templates/includes.html")
    result =  template.render(path, {
        "request_id": request_id,
        "js_path": "/gae_mini_profiler/static/js/profiler.js",
        "css_path": "/gae_mini_profiler/static/css/profiler.css",
        "show_immediately_js": json.dumps(show_immediately),
    })
    return result


@register.simple_tag
def profiler_includes():
    from gae_mini_profiler import profiler
    return profiler_includes_request_id(profiler.requeststore.get_id())

