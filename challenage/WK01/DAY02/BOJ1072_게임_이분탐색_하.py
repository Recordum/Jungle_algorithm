import sys

# y //(x + ans) || (y + ans) // (x + ans)
# ans x//100 ~ x 

# 오답 / 실버 3
# 접근은 맞았으나
# 나눌떄 // 으로 해야함 int() 로 감싸도 잘못계산될 수 있음
# 99% 이상일떄 를 제외해야함
def binary_search(start, end, x, y, compare):
    mid = (start + end) // 2
    if start > end:
        return start
    if compare == (y + mid) * 100 // (x + mid):
        return binary_search(mid + 1, end ,x, y, compare)
    else:
        return binary_search(start, mid-1, x, y, compare)

x, y = map(int, input().split())
compare = y * 100 // x
if compare >= 99:
    print(-1)
else:
    result = binary_search(1, x * 100, x, y, compare)
    print(result)