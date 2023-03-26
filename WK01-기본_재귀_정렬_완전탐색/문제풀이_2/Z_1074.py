import sys
input = sys.stdin.readline

def div_recursive(length, r ,c, number):
    if length == 1:
        return int(number)
    if r < length/2 and c < length/2:
        return div_recursive(length/2, r, c, number)
    if r < length/2 and c >= length/2:
        return div_recursive(length/2, r, c - length/2, number + (length/2)**2)
    if r >= length/2 and c < length/2:
        return div_recursive(length/2, r - length/2, c, number + 2 * (length/2)**2)
    if r >= length/2 and c >= length/2:
        return div_recursive(length/2, r - length/2, c - length/2, number + 3 * (length/2)**2)


n, r, c = map(int,input().split())
print(div_recursive(2**n, r, c, 0))