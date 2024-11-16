def suffixArr(s):
    n = len(s)
    suffixes = [(s[i:], i) for i in range(n)]
    suffixes.sort()
    return [suffix[1] for suffix in suffixes]


def lcpArr(s, sufArr):
    n = len(s)
    rank = [0] * n
    lcp = [0] * (n - 1)

    for i, si in enumerate(sufArr):
        rank[si] = i

    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = sufArr[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i] - 1] = h
            if h > 0:
                h -= 1

    return lcp


def solve(s):
    sArr = suffixArr(s)
    lcp = lcpArr(s, sArr)
    rp = 0
    for l in lcp:
        if l > 0:
            rp += l
    print(rp)


s = input()
solve(s)
