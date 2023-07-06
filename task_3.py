# Task 3

# A decorator named 'cache' that will store in memory the output of every particular call to a function. This way, if we call the function twice with the same input parameters, the function will not be called the second time and the result will be fetched from the cache instead.

# The function will also print Calculating when it is the first time we use a particular call and Using the cache in any other case.

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


def cache(func):
    cache_data = {}

    def wrap(*args, **kwargs):
        key = (args, tuple(kwargs.items()))

        if func in cache_data and key in cache_data[func]:
            print("Using the cache")
            return cache_data[func][key]

        print("Calculating")
        result = func(*args, **kwargs)

        if func not in cache_data:
            cache_data[func] = {}

        cache_data[func][key] = result
        return result

    return wrap


@debug
@validate_numeric
@cache
def sum(a, b):
    """Return the sum of two numbers."""
    return a + b


print(sum(1, 2))
print(sum(1, 2))
print(sum(3, 2))
print(sum(3, 2))
print(sum(2, 1))
