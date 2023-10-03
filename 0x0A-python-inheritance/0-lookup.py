#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object for which attributes and methods are to be looked up.

    Returns:
        list: A list of public attributes and methods of the object.
    """

    # Use dir() to get a list of attributes and methods
    attributes_and_methods = dir(obj)

    # Filter out any items that start with an underscore to exclude private attributes/methods
    public_attributes_and_methods = [item for item in attributes_and_methods if not item.startswith('_')]
    return public_attributes_and_methods
