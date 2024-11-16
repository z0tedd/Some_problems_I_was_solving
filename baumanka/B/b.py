def solve(d, s):
    dp = [0] * (s + 1)
    dp[0] = 1
    for x in d:
        for j in range(x, s + 1):
            dp[j] += dp[j - x]
    print(dp[s])


n = int(input())
d = list(map(int, input().split()))
s = int(input())

solve(d, s)
