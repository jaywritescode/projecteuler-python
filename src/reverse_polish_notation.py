from operator import add, sub, mul
from fractions import Fraction

class ReversePolishNotation:

    operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': Fraction
    }

    def __init__(self, calculation):
        """
        :params:
        calculation - the calculation as an array in RPN
        """
        self.calculation = calculation


    def perform(self):
        stack = []
        for i in self.calculation:
            if i in ReversePolishNotation.operators:
                if len(stack) < 2:
                    raise ValueError("Illegal argument: {}".format(self.calculation))
                stack.append(ReversePolishNotation.operators[i](stack.pop(), stack.pop()))
            else:
                stack.append(int(i))

        if len(stack) != 1:
            raise ValueError("Illegal argument: {} resolves to {}".format(self.calculation, stack))
        return stack[0]
