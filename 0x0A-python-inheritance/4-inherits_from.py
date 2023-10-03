#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The specified class.

    Returns:
        bool: True if obj is an instance of a subclass of a_class; otherwise, False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
