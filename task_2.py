# Task 2

# The previous code and now create an additional decorator named debug. This will let us get some information on the execution of the function without having to add print all over the body of the function.

# This decorator should simply output information about the input and output arguments. It should indicate both the positional and keyword arguments passed to the function and the output before returning it.

def validate_numeric(func):
    def wrap(*args, **kwargs):
        # This concatenates the positional arguments (args) with the values of the keyword arguments (kwargs.values()) into a single tuple. It combines all the arguments into one sequence.
        for arg in args + tuple(kwargs.values()):
            if not isinstance(arg, (int, float)):
                return "The input arguments must be numeric"
        return func(*args, **kwargs)

    return wrap


def debug(func):
    def wrap(*args, **kwargs):
        print("**********")
        if args:
            print(f"Positional arguments: {', '.join(map(str, args))}")
        else:
            print("There are no positional arguments")

        if kwargs:
            print(
                f"Keyword arguments: {', '.join(f'{k}={v}' for k, v in kwargs.items())}")
        else:
            print("There are no keyword arguments")

        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result

    return wrap


@debug
@validate_numeric
def sum(a, b):
    """Return the sum of two numbers."""
    return a + b


sum(1, 2)
sum(a=1, b=2)
sum(1, "a")
