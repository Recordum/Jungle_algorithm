import sys
input = sys.stdin.readline

word_set = set()
word_dict = dict()

t = int(input())

for i in range(t):
    word = input().rstrip()
    word_set.add(word)

word_list = list(word_set)
sorted_i = sorted(word_list)
word_sorted = sorted(sorted_i, key= lambda x: len(x))

for i in range(len(word_sorted)):
    print(word_sorted[i])