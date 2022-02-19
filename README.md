# Overloaded functions in python

This is an example of how overloaded functions can be implemented in python. The underlying idea is that functions are only called with keyword arguments and their type is matched according to the type hints in the function declaration. If no matching function can be found, an `AttributeError` is raised. 

Example:

```python
    >>> func(a=1, b=2)
    3
    >>> func(a=1, b=[2, 3])
    6
    >>> func(a=[3, 2], b=[2, 3, 4])
    12
    >>> func(a=[3, 2], b=(2, 3, 4))
    Traceback (most recent call last):
    AttributeError: Function parameters do not match any overloaded function
```

## Missing features

* Positional features
* Nested type hints such as `typing.List[int]`
* Different number of arguments
