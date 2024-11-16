from itertools import combinations


def solve(n, s, k):
    test = sum(s[:k])
    for sub in combinations(s, k):
        # print(sub)
        nsub = sorted(sub)
        d = [nsub[i + 1] - nsub[i] for i in range(k - 1)]
        # print(d)
        if len(set(d)) == 1:
            # print(sum(nsub))
            if sum(nsub) == test:
                return True
    return False


n, k = [int(x) for x in input().split()]
s = [int(x) for x in input().split()]
if solve(n, s, k):
    print("YES")
else:
    print("NO")
