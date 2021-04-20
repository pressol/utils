import warnings
import functools
import inspect

string_types = (type(b''), type(u''))

# stackoverflow.com/questions/2536307
def deprecated(func):
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        warnings.simplefilter('always', DeprecationWarning)
        warnings.warn("Call to deprecated function {}.".format(func.__name__),
                      category=DeprecationWarning,
                      stacklevel=2)
        warnings.simplefilter('default', DeprecationWarning)
        return func(*args, **kwargs)
    return new_func()

def deprecated2(reason="please use other function"):
    if isinstance(reason, string_types):
        def decorator(func1):
            if inspect.isclass(func1):
                fmt1 = "Call to deprecated class {name} ({reason})."
            else:
                fmt1 = "Call to deprecated function {name} ({reason})."

            @functools.wraps(func1)
            def new_func1(*args, **kwargs):
                warnings.simplefilter ('always', DeprecationWarning)
                warnings.warn (
                    fmt1.format (name=func1.__name__, reason=reason),
                    category=DeprecationWarning,
                    stacklevel=2
                )
                warnings.simplefilter ('default', DeprecationWarning)
                return func1(*args, **kwargs)
        return decorator
    elif inspect.isclass(reason) or inspect.isfunction(reason):
        func2 = reason
        if inspect.isclass(func2):
            fmt2 = "Call to deprecated class {name}."
        else:
            fmt2 = "Call to deprecated function {name}."

        @functools.wraps(func2)
        def new_func2(*args, **kwargs):
            warnings.simplefilter ('always', DeprecationWarning)
            warnings.warn (
                fmt2.format (name=func2.__name__),
                category=DeprecationWarning,
                stacklevel=2
            )
            warnings.simplefilter ('default', DeprecationWarning)
            return func2
        return new_func2
    else:
        raise TypeError(repr(type(reason)))


def warning(reason="this function will use up all your RAM is not uses sensitivly"):
    if isinstance(reason, string_types):
        def decorator(func1):
            if inspect.isclass(func1):
                fmt1 = "Call to sensitive class {name} ({reason})."
            else:
                fmt1 = "Call to sensitive function {name} ({reason})."

            @functools.wraps(func1)
            def new_func1(*args, **kwargs):
                warnings.simplefilter ('always', UserWarning)
                warnings.warn (
                    fmt1.format (name=func1.__name__, reason=reason),
                    category=UserWarning,
                    stacklevel=2
                )
                warnings.simplefilter ('default', UserWarning)
                return func1(*args, **kwargs)
        return decorator
    elif inspect.isclass(reason) or inspect.isfunction(reason):
        func2 = reason
        if inspect.isclass(func2):
            fmt2 = "Call to sensitive class {name}."
        else:
            fmt2 = "Call to sensitive function {name}."

        @functools.wraps(func2)
        def new_func2(*args, **kwargs):
            warnings.simplefilter ('always', UserWarning)
            warnings.warn (
                fmt2.format (name=func2.__name__),
                category=UserWarning,
                stacklevel=2
            )
            warnings.simplefilter ('default', UserWarning)
            return func2
        return new_func2
    else:
        raise TypeError(repr(type(reason)))



