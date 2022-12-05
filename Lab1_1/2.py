import argparse
import operator
import math

parser = argparse.ArgumentParser()
parser.add_argument("oper", type=str)
parser.add_argument("numbers", type=int, nargs="+")
args = parser.parse_args()

def func(oper, *args) -> str:
    try:
        funct = getattr(operator, oper)
    except Exception:
        try:
            funct = getattr(math, oper)
        except Exception:
            return AttributeError
    return funct(*args)


print(func(args.oper, *args.numbers))
