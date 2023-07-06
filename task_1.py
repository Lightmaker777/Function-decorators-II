# Task 1
# A decorator named validate_numeric to validate if the input arguments of a function are numeric (types int or float).
# If any of the arguments passed to the function are not numeric, it should return a message The input arguments must be numeric and stop execution. Otherwise, it should execute the decorated function normally.


def validate_numeric(func):
    def wrap(*args, **kwargs):
        # This concatenates the positional arguments (args) with the values of the keyword arguments (kwargs.values()) into a single tuple. It combines all the arguments into one sequence.
        for arg in args + tuple(kwargs.values()):
            if not isinstance(arg, (int, float)):
                return "The input arguments must be numeric"
        return func(*args, **kwargs)

    return wrap


@validate_numeric
def sum(a, b):
    """Return the sum of two numbers."""
    return a + b


print(sum(1, 2))
print(sum(1, "2"))
print(sum(a=1, b="a"))
print(sum(a=1, b=3.4))
