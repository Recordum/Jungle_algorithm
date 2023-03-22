from collections import deque
import sys

input=sys.stdin.readline

n, k = map(int, input().split())
coins = list(set(int(input()) for _ in range(n)))
used = [0 for _ in range(k+1)]

def bfs(coins, target):
    q = deque()
    for coin in coins:
        if coin <= target:
            q.append([coin, 1])
            used[coin] = 1

    while q:
        coin_sum, cnt = q.popleft()
        if target == coin_sum:
            return cnt
        for coin in coins:
            n_coin_sum = coin_sum + coin
            n_cnt = cnt + 1
            if n_coin_sum > target:
                continue
            elif not used[n_coin_sum]:
                used[n_coin_sum] = 1
                q.append([n_coin_sum, n_cnt])
    return -1

ans = bfs(coins, k)

print(ans)