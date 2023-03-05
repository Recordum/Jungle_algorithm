import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    count = n
    if n >= 100:
        count = 99
        for i in range(100, n+1):
            parse_to_units = str(i)
            differ = 0
            i = len(parse_to_units) -1
            if i > 2:
                continue
            if int(parse_to_units[i-1]) - int(parse_to_units[i-2])  == int(parse_to_units[i]) - int(parse_to_units[i-1]):
                count+=1
    print(count)