import sys
input = sys.stdin.readline

n = int(input())
meeting_schedule = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x : (x[1],x[0]))
count = 1
end_time = meeting_schedule[0][1]
if not end_time:
    print(0)
    exit()
for i in range(1, len(meeting_schedule)):
    start = meeting_schedule[i][0]
    end = meeting_schedule[i][1]
    if end_time <= start:
        count += 1
        end_time = end
print(count)
