import sys
input = sys.stdin.readline

first_str = input().rstrip()
second_str = input().rstrip()
suffix_str = first_str + second_str
suffix_arr = [suffix_str[i:] for i in range(len(suffix_str))]
suffix_arr.sort()
for i in range(1,len(suffix_arr)):
    pre_str = suffix_arr[i-1]
    post_str = suffix_str[i]
