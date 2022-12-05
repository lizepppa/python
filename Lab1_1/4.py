import argparse


def maxw(W, w, n):
    subp_list = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for index in range(1, n + 1):
        for value in range(W + 1):
            if w[index - 1] <= value:
                subp_list[index][value] = max(w[index - 1] + subp_list[index - 1][value - w[index - 1]],
                                              subp_list[index - 1][value])
            else:
                subp_list[index][value] = subp_list[index - 1][value]
    return subp_list[n][W]


parser = argparse.ArgumentParser()
parser.add_argument("-W", type=int)
parser.add_argument("-w", nargs='+', type=int)
parser.add_argument("-n", type=int)
args = parser.parse_args()
print(maxw(args.W, args.w, args.n))
