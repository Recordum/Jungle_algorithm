t = int(input())
results = []
for i in range(t):
    n , str_iter = map(str,input().split())
    reverse_new_str = ""
    for i in range(len(str_iter)):
        reverse_new_str = reverse_new_str + str_iter[i] * int(n)

    results.append(reverse_new_str)


for result in results:
    print(result)