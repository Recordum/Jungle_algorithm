import sys
input = sys.stdin.readline


student_number = dict()
n = int(input())
m = int(input())
nominated = []
recommand = list(map(int, input().split()))
for num in recommand:
    if not num in student_number:
        student_number[num] = 1
    else:
        student_number[num] += 1
    if len(nominated) < n and not num in nominated:
       nominated.append(num)
    elif num in nominated:
        continue
    else:
        min = 1e9
        fail = 1e9
        for index, candidate in enumerate(nominated):
            if min > student_number[candidate]:
                min = student_number[candidate]
                fail = candidate
            if index == len(nominated) - 1: 
                nominated.remove(fail)
        nominated.append(num)
        student_number[fail] = 0
nominated.sort()
print(' '.join(map(str, nominated)))