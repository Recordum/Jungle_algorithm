import sys
input = sys.stdin.readline

def dfs(start, depth, number):
    global result

    if visited[start]:
        return
    visited[start] = True

    if depth == n:
        if result < number:
            result = number
            return

    for i in range(n):
        if visited[i]:
            continue
        dfs(i, depth+1, number + abs(a[start] - a[i]))
        visited[i] = False
    return




if __name__ == '__main__':
    n = int(input())
    result = 0
    a = list(map(int,input().split()))
    visited =[False] * n
    for start in range(n):
        visited =[False] * n
        dfs(start, 1, 0)
    print(result)


