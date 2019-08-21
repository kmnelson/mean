
from math import sqrt, log
from contracts import contract, new_contract

def mean(num_list):
    assert isinstance(num_list, (list, tuple))
    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError:
        return 0
    except TypeError as detail:
        msg = "The algebraic mean of an non-numerical list is undefined.\nPlease provide a list of numbers."
        raise TypeError(detail.__str__() + "\n" +  msg)

def perfect_sqrt(x):
    retval = sqrt(x)
    iretval = int(retval)
    return iretval if iretval == retval else retval


def perfect_sqrt2(x):
    return int(sqrt(x))

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
