n = []
count = [0] * 10
for i in range(3):
    n.append(int(input()))

multiply = str(n[0] * n[1] * n[2])

for i in range(len(multiply)):
    count[int(multiply[i])] +=1

for i in range(len(count)):
    print(count[i])







