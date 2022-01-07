def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Returns:
        A value, of same type of elements in the iterable parameter.
        None if the iterable can not be used by the function.
    """

    it = iter(iterable)
    try:
        initializer = next(it)
    except StopIteration:
        raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function_to_apply(accum_value, x)
    return accum_value