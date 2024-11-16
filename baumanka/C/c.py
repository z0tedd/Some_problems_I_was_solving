import heapq


def solve(n, m, index):
    graph = {i: [] for i in range(n)}
    for _ in range(m):
        x, y, z = map(int, input().split())
        graph[x].append((y, z))
        graph[y].append((x, z))
    d = [10**9] * n
    d[index] = 0
    pq = [(0, index)]
    while pq:
        ct, cn = heapq.heappop(pq)
        if ct > d[cn]:
            continue
        for nb, t in graph[cn]:
            nt = ct + t
            if nt < d[nb]:
                d[nb] = nt
                heapq.heappush(pq, (nt, nb))
    mn = max(d)
    if mn == 10**9:
        print(-1)
        return
    print(mn)


n, m = map(int, input().split())
index = int(input())

solve(n, m, index)
