import sys
input = sys.stdin.readline

n = int(input())
input_str = input().rstrip()
number = set('1234567890')
hidden_number = ''
result  = 0
for i in range(n):
    if input_str[i] in number:
        hidden_number += input_str[i] 
    else:
        if hidden_number != '':
            result += int(hidden_number)
            hidden_number = ''

if hidden_number != '':
    result += int(hidden_number)
    
print(result)
