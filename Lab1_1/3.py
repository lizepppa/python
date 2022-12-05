import argparse


def check(formula):
    if (formula):
        if formula[-1] in ("+", "-") or formula[0] in ("+", "-"):
            print("False, None")
        else:
            for i in range(1, len(formula) + 1):
                if len(formula) == i:
                    print("True,", eval(formula))
                    break
                elif formula[i - 1] in ("+", "-") and formula[i] in ("+", "-"):
                    print("False, None")
                    break
    else:
        print("False, None")


parser = argparse.ArgumentParser()
parser.add_argument("formula", nargs="?", type=str)
args = parser.parse_args()
check(args.formula)
