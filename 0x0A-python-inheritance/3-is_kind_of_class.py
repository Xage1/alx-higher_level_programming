#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of or inherited from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if the object is an instance of or inherited from the specified class, False otherwise.
    """
    return isinstance(obj, a_class)

