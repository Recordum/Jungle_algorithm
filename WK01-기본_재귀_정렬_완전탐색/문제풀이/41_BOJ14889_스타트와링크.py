import sys

def dfs_team(member, depth):
    global result
    if visited[member]:
        return

    visited[member] = True

    if depth == n/2:
        start_score = 0
        link_score = 0
        for i in range(len(visited)-1):
            for j in range(i + 1, len(visited)):
                if visited[i] and visited[j]:
                    start_score = start_score + score_map[i][j] + score_map[j][i]
                elif not visited[i] and not visited[j]:
                    link_score = link_score + score_map[i][j] + score_map[j][i]

        if result > abs(link_score - start_score):
            result = abs(link_score - start_score)
        return

    for i in range(member, n):
        if not visited[i]:
            dfs_team(i, depth+1)
            visited[i] = False

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    result = int(1e9)
    score_map = [] * n
    visited = [False] * n
    for i in range(n):
        score_map.append(list(map(int,input().split())))
    dfs_team(0,1)
    print(result)




