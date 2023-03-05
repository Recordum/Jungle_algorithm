import sys
input = sys.stdin.readline


def traver_map(start_city, cost, depth, start_flag):
    global result_cost
    visited[start_city] = True

    if depth == n-1 and cost_map[start_city][start_flag] != 0:
        cost = cost + cost_map[start_city][start_flag]
        if result_cost > cost:
            result_cost = cost
        return

    for i in range(len(next_city)):
        if visited[next_city[i]] or cost_map[start_city][next_city[i]] == 0:
            continue
        visited[next_city[i]] = True
        traver_map(next_city[i], cost + cost_map[start_city][next_city[i]], depth + 1, start_flag)
        visited[next_city[i]] = False
    return




if __name__ == '__main__':
    n = int(input())
    cost_map = []
    result_cost = sys.maxsize
    next_city = [i for i in range(n)]

    for i in range(n):
        cost_map.append(list(map(int,input().split())))

    for i in range(n):
        visited = [False]*n
        depth = 0
        cost = 0
        start_flag = i
        start_city = i
        traver_map(start_city, cost, depth, start_flag)

    print(result_cost)

