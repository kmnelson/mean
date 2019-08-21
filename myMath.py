
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

@contract(x='int,>=0',returns='int,>=0')
def perfect_sqrt(x):
    retval = sqrt(x)
    iretval = int(retval)
    return iretval if iretval == retval else retval


@new_contract
def ends_ok(x):
    ends14569 = x%10 in (1,4,5,6,9)
    ends00 = int(round((log(x,10)))) % 2 == 0
    if ends14569 or ends00:
        return True
    raise ValueError("%s doesn't end in 1,4,5,6 or 9 or even number of zeros"%x)


@contract(x='int,ends_ok,>=0',returns='int,>=0')
def perfect_sqrt2(x):
    return int(sqrt(x))

@contract(n='int,>=0')
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
