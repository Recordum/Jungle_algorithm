import sys
input = sys.stdin.readline


n, m = map(int, input().split())

cards = list(map(int,input().split()))
result = 0

for i in range(len(cards)):
    for j in range(i+1,len(cards)):
        for k in range(j+1, len(cards)):
            sum_cards = cards[i] + cards[j] + cards[k]
            if m - sum_cards >= 0 and m - sum_cards < m - result:
                result = sum_cards

print(result)

