t = int(input())
results = []
for i in range(t):
    n , str_iter = map(str,input().split())
    new_str = ""
    for i in range(len(str_iter)):
        new_str = new_str + str_iter[i] * int(n)

    results.append(new_str)


for result in results:
    print(result)