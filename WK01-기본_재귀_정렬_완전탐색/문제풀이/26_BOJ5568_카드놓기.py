from itertools import permutations

n = int(input())
k = int(input())
s = set()

cards = []
for i in range(n):
    cards.append(str(input()))
for card in permutations(cards, k):
    new_card=""
    for i in range(k):
        new_card = new_card + card[i]
    s.add(new_card)

print(len(s))
