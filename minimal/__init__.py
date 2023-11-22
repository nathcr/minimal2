def my_sum(x, y):
    """A function that sums. """
    return x+y


def my_mul(x, y):
    """A function that multiply. """
    return x*y

from sympy import init_printing, symbols
from sympy import diff, exp
x, y = symbols('x y')

def rtang(x1,x0):
  expr=diff(x1)
  a=expr.subs({x:x0})
  return (y-x0,a*(x-x0))





