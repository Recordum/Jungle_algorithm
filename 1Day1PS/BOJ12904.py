import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

while True:
    if s == t:
        break
    if s + ["A"] == t[0:len(s)+1] or s + ["A"] == list(reversed(t[:-len(s)-2:-1])):
        s.append("A")
        continue
    if list(reversed(s)) + ["B"] == t[0:len(s)+1] or list(reversed(s)) + ["B"] == list(reversed(t[:-len(s)-2:-1])):
        s = list(reversed(s)) + ["B"]
        continue
    print(0)
    exit()

print(1)

