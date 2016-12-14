import sys

from datetime import datetime, timedelta
from fractions import gcd

def timed(func):
    """
    Wrap a function in a timer.
    """
    def timed_func(*args, **kwargs):
        now = datetime.now
        s_0 = now()
        value = func(*args, **kwargs)
        s_1 = now()
        print('%s' % (s_1 - s_0))
        return value
    return timed_func

class memoize(dict):
    """
    https://wiki.python.org/moin/PythonDecoratorLibrary#Alternate_memoize_as_dict_subclass
    """
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result

@memoize
def gcd_(a, b):
    return gcd(a, b)

def mult(a, b):
    return a*b

@memoize
def inner(k1, k2):
    D = gcd_(k1, k2)
    return sum([k1//t for t in range(1, gcd_(k1,k2)+1) if D//t == D/t])

@memoize
def p(a, b):
    if b > a:
        return p(b, a)
    if(a==0 and b==0):
        return 1
    if(b==0):
        return 0
    if(a==1 or b==1):
        return 1
    if(b==2):
        return a//2 + 1
    return sum([
        mult(p(a-k1, b-k2), inner(k1, k2))
        for k1 in range(1,a+1)
        for k2 in range(1,b+1)
    ])//a

if __name__ == "__main__":
    NN = int(sys.argv[-1]) 
    """
    If this script were any more complicated
    then I would have used argparse.
    """
    data = timed(lambda N:[[p(x, y) for y in range(1,N)] for x in range(1,N)])(NN)
    print([data[i][i] for i in range(len(data[0]))])
