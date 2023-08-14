import sys
# 정답 / 실버 5
# 간단한 구현문제 그러나 리스트에 저장할때 
# total값이 index를 넘는다는걸 유의하지 않아 index out of bound 에러 발생
number_list = [False] * 10001

for i in range(1, 10001):
    units = list(map(int, str(i)))
    total = i + sum(units)
    if total <= 10000:
        number_list[total] = True

for index, number in enumerate(number_list):
    if number == False and not index == 0:
        print(index)
