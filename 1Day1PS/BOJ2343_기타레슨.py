import sys
input = sys.stdin.readline

def binary_search(count, start, end):
    mid = (start + end)//2 # 총합의 mid
    total = 0
    blurray = 0
    if start > end:
        return start
    for lecture in lectures:
        if total + lecture > mid:
            total = 0
            blurray += 1
        total += lecture
    if total != 0:
        blurray += 1

    if blurray > count:
        return binary_search(count, mid + 1, end)
    else:
        return binary_search(count, start , mid-1)

n ,m = map(int, input().split())
lectures = list(map(int, input().split()))
lectures_sorted = sorted(lectures)
print(binary_search(m,lectures_sorted[-1],sum(lectures)))
