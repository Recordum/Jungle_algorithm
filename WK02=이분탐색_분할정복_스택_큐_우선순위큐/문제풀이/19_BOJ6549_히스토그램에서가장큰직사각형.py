import sys
input = sys.stdin.readline


def divided_histogram(start, end):
    global result
    mid = (start+end)//2
    if end - start == 0:
        result = max(result,histogram_list[start])
        return
    divided_histogram(start,mid)
    divided_histogram(mid+1,end)
    left_move = mid
    right_move = mid
    height = histogram_list[mid]
    while left_move > start and right_move < end:
        if histogram_list[left_move-1] > histogram_list[right_move+1]:
            left_move -= 1
            height = min(height,histogram_list[left_move])
        else:
            right_move += 1
            height = min(height,histogram_list[right_move])

        result = max(height * (right_move - left_move + 1),result)

    while right_move < end:
        right_move += 1
        height = min(height, histogram_list[right_move])
        result = max(height * (right_move - left_move + 1),result)

    while left_move > start:
        left_move -= 1
        height = min(height, histogram_list[left_move])
        result = max(height * (right_move - left_move + 1),result)

    return
answer = []
while True:
    result = 0
    input_list = list(map(int, input().split()))
    n = input_list[0]
    if n == 0:
        break
    histogram_list = list(input_list[1:])
    divided_histogram(0,len(histogram_list)-1)
    answer.append(result)

for ans in answer:
    print(ans)
