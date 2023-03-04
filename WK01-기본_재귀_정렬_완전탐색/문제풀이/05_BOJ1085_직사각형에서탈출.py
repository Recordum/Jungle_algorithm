x,y,w,h = map(int, input().split())

array = []

array.append(w-x)
array.append(x)
array.append(h-y)
array.append(y)

print(min(array))
