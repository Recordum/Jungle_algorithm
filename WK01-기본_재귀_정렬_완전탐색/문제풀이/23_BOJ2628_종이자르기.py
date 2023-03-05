import sys

input = sys.stdin.readline

if __name__ == '__main__':

    horizontal = []
    vertical = []
    n, m = map(int, input().split())

    t = int(input())

    vertical.append(n)
    horizontal.append(m)

    for i in range(t):
        direction, val = map(int, input().split())
        if direction == 0:
            horizontal.append(val)
        else:
            vertical.append(val)

    sorted_horizontal = sorted(horizontal, reverse=True)
    sorted_vertical = sorted(vertical, reverse=True)
    cut_n = []
    cut_m = []
    if len(sorted_vertical) == 1:
        cut_n.append(n)
    if len(sorted_horizontal) == 1:
        cut_m.append(m)

    for i in range(1, len(sorted_vertical)):
        val = sorted_vertical[i - 1] - sorted_vertical[i]
        cut_n.append(val)
        if i == len(sorted_vertical) - 1:
            cut_n.append(sorted_vertical[i])

    for i in range(1, len(sorted_horizontal)):
        val = sorted_horizontal[i - 1] - sorted_horizontal[i]
        cut_m.append(val)
        if i == len(sorted_horizontal) - 1:
            cut_m.append(sorted_horizontal[i])

    result = max(cut_n) * max(cut_m)

    print(result)
