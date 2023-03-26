import sys
input = sys.stdin.readline


n = int(input())
account_list = []

for _ in range(n):
    account = int(input())
    if account != 0:
        account_list.append(account)
    else :
        account_list.pop()


print(sum(account_list))