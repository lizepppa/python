import argparse


parser = argparse.ArgumentParser()
parser.add_argument("num1", type=int)
parser.add_argument("oper", type=str)
parser.add_argument("num2", type=int)
args = parser.parse_args()
if args.oper not in ("+", "-", "*", "/"):
    print("Not math symbol")
elif args.oper in ("+", "-", "*"):
    print("Result is:", eval(str(args.num1) + args.oper + str(args.num2)))
elif args.oper == "/" and args.num2 == "0":
    print("Division by zero")
else:
    print(eval(str(args.num1) + args.oper + str(args.num2)))
