from django import template
register = template.Library()

def do_get_url(parser, token):
    bits = token.split_contents()
    if len(bits) < 4: 
        raise template.TemplateSyntaxError("'%s' takes at least one argument"
                                  " (path to a view)" % bits[0])
    app_name = bits[1]
    action_type = bits[2]
    obj_name = bits[3]
    args = [] 
    kwargs = {} 
    asvar = None 

    if len(bits) > 4: 
        bits = iter(bits[4:])
        for bit in bits:
            if bit == 'as':
                asvar = bits.next()
                break
            else:
                for arg in bit.split(","):
                    if '=' in arg: 
                        k, v = arg.split('=', 1)
                        k = k.strip()
                        kwargs[k] = parser.compile_filter(v)
                    elif arg: 
                        args.append(parser.compile_filter(arg))
    return GetURLNode(app_name, action_type[1:-1], obj_name, args, kwargs, asvar)
do_get_url = register.tag("get_url", do_get_url)


class GetURLNode(template.Node):
    def __init__(self, app_name, action_type, obj_name, args, kwargs, asvar):
        self.app_name = app_name
        self.action_type = action_type
        self.obj_name = obj_name
        self.args = args
        self.kwargs = kwargs
        self.asvar = asvar
        
#    def render(self, context):
      #  reverse_url = template.Variable(self.app_name).resolve(context) + self.action_type + template.Variable(self.obj_name).resolve(context)
      #  return reverse(reverse_url)
    def render(self, context):
        from django.core.urlresolvers import reverse, NoReverseMatch
        args = [arg.resolve(context) for arg in self.args]
        kwargs = dict([(smart_str(k,'ascii'), v.resolve(context))
                       for k, v in self.kwargs.items()])
        reverse_url = template.Variable(self.app_name).resolve(context) + self.action_type + template.Variable(self.obj_name).resolve(context)
        # Try to look up the URL twice: once given the view name, and again
        # relative to what we guess is the "main" app. If they both fail,
        # re-raise the NoReverseMatch unless we're using the
        # {% url ... as var %} construct in which cause return nothing.
        url = ''
        try:
            url = reverse(reverse_url, args=args, kwargs=kwargs, current_app=context.current_app)
        except NoReverseMatch, e:
            if settings.SETTINGS_MODULE:
                project_name = settings.SETTINGS_MODULE.split('.')[0]
                try:
                    url = reverse(project_name + '.' + reverse_url,
                              args=args, kwargs=kwargs, current_app=context.current_app)
                except NoReverseMatch:
                    if self.asvar is None:
                        # Re-raise the original exception, not the one with
                        # the path relative to the project. This makes a
                        # better error message.
                        raise e
            else:
                if self.asvar is None:
                    raise e

        if self.asvar:
            context[self.asvar] = url
            return ''
        else:
            return url
