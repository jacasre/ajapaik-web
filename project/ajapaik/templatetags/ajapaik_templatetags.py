from django.template import Library, Node, Variable, resolve_variable, TemplateSyntaxError
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.text import normalize_newlines
from django.contrib.contenttypes.models import ContentType
import re

from project import settings
from django_comments_xtd import get_model as get_comment_model

XtdComment = get_comment_model()
register = Library()


class AddGetParameter(Node):
    def __init__(self, values):
        self.values = values

    def render(self, context):
        req = resolve_variable('request', context)
        params = req.GET.copy()
        for key, value in self.values.items():
            params[key] = value.resolve(context)
        return '?%s' % params.urlencode()


@register.tag
def add_get(parser, token):
    pairs = token.split_contents()[1:]
    values = {}
    for pair in pairs:
        s = pair.split('=', 1)
        values[s[0]] = parser.compile_filter(s[1])
    return AddGetParameter(values)


class GetXtdCommentTreeNode(Node):
    def __init__(self, obj, var_name):
        self.obj = Variable(obj)
        self.var_name = var_name

    def render(self, context):
        obj = self.obj.resolve(context)
        ctype = ContentType.objects.get_for_model(obj)
        qs = XtdComment.objects.filter(content_type=ctype,
                                       object_pk=obj.pk,
                                       site__pk=settings.SITE_ID,
                                       is_public=True)
        diclist = XtdComment.full_tree_from_queryset(qs)
        context[self.var_name] = diclist
        return ''


@register.tag
def get_xtdcomment_full_tree(parser, token):
    try:
        tag_name, args = token.contents.split(None, 1)
    except ValueError:
        raise TemplateSyntaxError("%s tag requires arguments" %
                                  token.contents.split()[0])
    match = re.search(r'for (\w+) as (\w+)', args)
    if not match:
        raise TemplateSyntaxError("%s tag had invalid arguments" % tag_name)
    obj, var_name = match.groups()
    return GetXtdCommentTreeNode(obj, var_name)


@register.simple_tag
def settings_value(name):
    return getattr(settings, name, '')


@register.filter
def div(value, arg):
    try:
        value = int(value)
        arg = int(arg)
        if arg: return value / arg
    except:
        pass
    return ''


def remove_newlines(text):
    normalized_text = normalize_newlines(text)
    return mark_safe(normalized_text.replace('\n', ' '))

remove_newlines.is_safe = True
remove_newlines = stringfilter(remove_newlines)
register.filter(remove_newlines)
