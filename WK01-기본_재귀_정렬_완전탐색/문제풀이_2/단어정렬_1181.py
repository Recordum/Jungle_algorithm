import sys
input = sys.stdin.readline

n = int(input())
words_list = list(set(input().rstrip() for _ in range(n)))
sorted_words_list = sorted(words_list, key= lambda x : (len(x),x))

for word in sorted_words_list:
    print(word)