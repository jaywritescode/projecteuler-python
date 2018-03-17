from collections import Counter

def congruent(*args):
    """
    Determine if k numbers contain the same digits in the same frequency.

    Args:
        *args (int|str): the numbers

    Returns:
        bool: True iff each digit appears the same number of times (possibly
            zero) in all of the arguments.
    """
    if len(args) < 2:
        return True
    counter = Counter(str(args[0]))
    return all(Counter(str(n)) == counter for n in args[1:])

def digits(number):
    """
    Convert a number into a list of its constituent digits.

    Args:
        number (int): a number

    Returns:
        list: a list of int, the digits in *number*
    """
    if number is 0:
        return [0]

    num = abs(number)
    digits = []
    while num > 0:
        digits = [num % 10] + digits
        num //= 10
    return digits
