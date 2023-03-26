import math
import sys

input = sys.stdin.readline().rstrip()
a,b,v = map(int,input.split())

count = int(math.ceil((v-a)/(a-b))) + 1

print(count)
