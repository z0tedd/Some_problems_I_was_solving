from itertools import combinations
from itertools import permutations

from itertools import permutations


def solve(n, t, a):
    for perm in permutations(a):
        if solveHelper("", t, 1, perm[0], perm):
            return True
    return False


def solveHelper(op, t, index, s, a):
    if s == t:
        return True
    if index == len(a):
        return False

    if op == "+":
        s = s + a[index]
    elif op == "-":
        s = s - a[index]
    elif op == "*":
        s = s * a[index]
    elif op == "/":
        if a[index] == 0:
            return False
        s = s // a[index]

    return any(
        (
            solveHelper("+", t, index + 1, s, a),
            solveHelper("-", t, index + 1, s, a),
            solveHelper("*", t, index + 1, s, a),
            solveHelper("/", t, index + 1, s, a),
        )
    )


n, t = map(int, input().split())
a = list(map(int, input().split()))
if solve(n, t, a):
    print("YES")
else:
    print("NO")
