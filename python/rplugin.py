class Proxy:
    def __init__(self, component):
        self.component = component
        self.__class__ = self.__class__.extend(component.__class__)

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


class Neovim(Proxy):
    def call(self, name, *args):
        return self.Function(name)(*args)
