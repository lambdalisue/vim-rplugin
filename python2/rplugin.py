class Proxy:
    def __init__(self, component):
        self._component = component
        self.__class__ = build_proxy(self, component)


class FuncNamespace:
    __slots__ = ['vim']

    def __init__(self, vim):
        self.vim = vim

    def __getattr__(self, name):
        return self.vim.Function(name)


class Neovim(Proxy):
    def __init__(self, vim):
        self.funcs = FuncNamespace(vim)
        super().__init__(vim)

    def call(self, name, *args):
        return self.Function(name)(*args)


def build_proxy(child, parent):
    proxy = type(
        "%s:%s" % (
            type(parent).__name__,
            child.__class__.__name__,
        ),
        (child.__class__,), {}
    )
    child_class = child.__class__
    parent_class = parent.__class__

    def bind(attr):
        if hasattr(child_class, attr) or not hasattr(parent_class, attr):
            return

        ori = getattr(parent_class, attr)

        def mod(self, *args, **kwargs):
            return ori(self._component, *args, **kwargs)

        setattr(proxy, attr, mod)

    for attr in parent_class.__dict__.keys():
        bind(attr)

    return proxy
