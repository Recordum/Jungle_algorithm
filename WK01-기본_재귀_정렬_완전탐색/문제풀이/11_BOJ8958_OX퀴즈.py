t = int(input())

q = []
results = [0] * t
count = 0

for i in range(t):
    q.append(input())

for i in range(len(q)):
    for j in range(len(q[i])):
        if q[i][j] == 'O':
            count += 1
            results[i] = results[i] + count

        if q[i][j] == 'X':
            count = 0
    count = 0

for result in results:
    print(result)


