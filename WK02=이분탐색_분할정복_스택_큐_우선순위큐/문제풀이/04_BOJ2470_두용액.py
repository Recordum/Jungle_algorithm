import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def binary_mixture(start,end):
    global result

    if end <= start:
        return
    ph_mixture = ph_list[start] + ph_list[end]

    if result > abs(ph_mixture):
        result = abs(ph_mixture)
        answer[0] = ph_list[start]
        answer[1] = ph_list[end]

    if ph_mixture == 0:
        return
    if ph_mixture < 0:
        return binary_mixture(start+1, end)
    if ph_mixture > 0:
        return binary_mixture(start, end-1)

n = int(input())
ph_list = sorted(list(map(int, input().split())))
start = 0
end = len(ph_list)-1
result = sys.maxsize
answer = [0] * 2
binary_mixture(start, end)
for i in sorted(answer):
    print(i, end=' ')

# while start < end:
#     ph_mixture = ph_list[start] + ph_list[end]
#     if result > abs(ph_mixture):
#         result = abs(ph_mixture)
#         answer = ph_list[start], ph_list[end]
#     if ph_mixture == 0:
#         break
#     if ph_mixture < 0:
#         start += 1
#     else:
#         end -= 1



