import sys
input = sys.stdin.readline


def decode(count, index):
    global result
    global decode_length
    string_count = 0

    for i in range(index, len(n)):
        if not visited[i]:

            string_count += 1

            visited[i] = True
            if n[i] == '(':
                string_count -= 2
                decode(n[i-1], i +1)
                string_count = string_count + decode_length



            if n[i] == ')':
                string_count -= 1
                decode_length = int(count) * string_count
                return

    result = string_count
    return




decode_length = 0
n = input().rstrip()
visited = [False] * len(n)
result = 0
decode(0, 0)
print(result)
