import vim


# NOTE:
# vim.options['encoding'] returns bytes so use vim.eval('&encoding')
ENCODING = vim.eval('&encoding')


def reform_bytes(value):
    if isinstance(value, bytes):
        return value.decode(ENCODING, 'surrogateescape')
    elif isinstance(value, (dict, vim.Dictionary, vim.Options)):
        return {
            reform_bytes(k): reform_bytes(v) for k, v in value.items()
        }
    elif isinstance(value, (list, tuple, vim.List)):
        return list(map(reform_bytes, value))
    else:
        return value


class Proxy:
    def __init__(self, component):
        self.component = component
        self.__class__ = self.__class__.extend(component.__class__)

    def __getattr__(self, name):
        value = getattr(self.component, name)
        return self.__class__.decorate(value)

    @classmethod
    def extend(cls, component_cls):
        decorator = type('ProxyExtended', (cls,), {})

        def bind(attr):
            if hasattr(decorator, attr) or not hasattr(component_cls, attr):
                return
            ori = getattr(component_cls, attr)

            def mod(self, *args, **kwargs):
                return ori(self.component, *args, **kwargs)

            setattr(decorator, attr, mod)

        for attr in component_cls.__dict__.keys():
            bind(attr)
        return decorator

    @classmethod
    def decorate(cls, component):
        if component in (vim.buffers, vim.windows, vim.tabpages, vim.current):
            return Proxy(component)
        elif isinstance(component, (vim.Buffer, vim.Window, vim.TabPage)):
            return Proxy(component)
        elif isinstance(component, (vim.List, vim.Dictionary, vim.Options)):
            return ContainerProxy(component)
        return component


class ContainerProxy(Proxy):
    def __getitem__(self, key):
        return reform_bytes(self.component[key])

    def __setitem__(self, key, value):
        if isinstance(value, str):
            value = value.encode(ENCODING)
        self.component[key] = value


class Neovim(Proxy):
    def call(self, name, *args):
        return reform_bytes(self.Function(name)(*args))
