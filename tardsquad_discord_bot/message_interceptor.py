class InterceptorMetaclass(type):
    """Collects @message_interceptor annotated method to a list for later usage in the class.

    Reference: https://stackoverflow.com/a/60956561/265508
    """

    def __init__(cls, name, bases, attrs):
        cls.interceptor_methods = []
        for key, val in attrs.items():
            if getattr(val, "_interceptor_method", None):
                cls.interceptor_methods.append(val)


def message_interceptor():
    """
    Creates an attribute on the method, so it can
    be discovered by the metaclass
    """

    def decorator(f):
        f._interceptor_method = True
        return f

    return decorator
