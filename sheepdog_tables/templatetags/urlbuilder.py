from django import template
from django.core.urlresolvers import reverse 

register = template.Library()


class UrlBuilderNode(template.Node):
    """
    urlbuilder is a template tag that takes a :py:class:`TableRowURL` object
    and an object to get data from, like a Participant or Connector.
    It builds a list of arguments from the args parameter as found in
    :py:class:`TableRowURL`.  For each one, it checks if the argument matches a
    property of the passed object, and will use that property.  Otherwise
    it will just pass through the argument as is.

    The result is a URL, like /myapp/myobject/1/, generated at the end of
    the day, by django.core.urlresolvers.reverse

    Usage for this template tag are as follows:

    ::

        {% urlbuilder tablerowurl object %}

    :param url: A :py:class:`TableRowURL` object or matching subclass
    :param obj: A (normally) model backed object.

    """
    def __init__(self, url, obj):
        self.url = url
        self.obj = obj

    def render(self, context):
        """
        Render's a URL based off a given URL object and model object

        :param context: The current template context
        :return: The URL or ""
        """
        try:
            url = context.get(self.url, None)
            obj = context.get(self.obj, None)

            if url is None or obj is None:
                return ''

            arg_lists = [arg.split('.') for arg in url.args]
            args = []
            # TODO: Replace with resolve() when it gets implemented.
            for arg_list in arg_lists:
                chain = obj
                for arg in arg_list:
                    chain = getattr(chain, arg) if hasattr(chain, arg) else arg
                    chain = chain() if callable(chain) else chain
                args.append(chain)

            return reverse(url.url, args=args)
        except template.VariableDoesNotExist:
            return ""


def urlbuilder(parser, token):
    """
    :param parser: Set for utility.
    :param token: The passed token to render from.
    """
    try:
        tag_name, url, obj = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError('%s requires 2 arguments' % tag_name)
    return UrlBuilderNode(url, obj)

register.tag('urlbuilder', urlbuilder)

