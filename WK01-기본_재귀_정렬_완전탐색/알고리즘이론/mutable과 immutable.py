A = "a"
A_1 = "a"

print(id(A))
print(id(A_1))


array_1 = [1,2]
array_2 = [1,2]

print(id(array_1))
print(id(array_2))
print(array_1 is array_2)
print(array_1 == array_2)

print(id(array_1[0]))
print(id(array_2[0]))
