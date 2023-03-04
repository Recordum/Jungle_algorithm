n,m = map(str,input().split())

result = max(int(n[::-1]),int(m[::-1]))

print(result)