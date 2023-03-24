import sys
input = sys.stdin.readline

test_case = int(input())
result = []
for t in range(test_case):
    n = int(input())
    grade = [list(map(int, input().split())) for _ in range(n)]
    sorted_by_letter = sorted(grade)
    interview_grade = sorted_by_letter[0][1]
    count = 1
    for letter, interview in sorted_by_letter:
        if interview_grade > interview:
            count += 1
            interview_grade = interview
    result.append(count)
for ans in result:
    print(ans)

