import sys
input = sys.stdin.readline

def binary_search(number , start, end):
    mid = (start + end)//2
    if start > end:
        return False
    if card_list[mid] == number:
        return True
    if card_list[mid] <= number:
        return binary_search(number, mid + 1, end)
    else:
        return binary_search(number, start, mid - 1)

n = int(input())
card_list = list(map(int, input().split()))
m = int(input())
number_list = list(map(int, input().split()))

card_list.sort()
result = [0 for _ in range(m)]
for index, number in enumerate(number_list):
    if binary_search(number, 0, len(card_list) - 1):
        result[index] = 1

print(" ".join(map(str, result)))