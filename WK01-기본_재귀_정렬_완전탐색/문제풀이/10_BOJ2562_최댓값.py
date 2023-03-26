A = []

for i in range(9):
    A.append(int(input()))

result = A.index(max(A))

print(max(A))
print(result + 1)