import sys


def _mode():
    for i in range(len(number_list)):
        count_sort[number_list[i]] += 1
    for i in range(len(count_sort)):
        if count_sort[i] == max(count_sort):
            if i > 4000:
                count.append(i - 8001)
            else:
                count.append(i)
    count.sort()
    return


if __name__ == '__main__':
    input = sys.stdin.readline
    count = []
    n = int(input())
    count_sort = [0] * 8001
    number_list = [int(input()) for _ in range(n)]
    number_list.sort()
    print(round(sum(number_list) / len(number_list)))
    print(number_list[int(len(number_list) / 2)])
    _mode()
    if len(count) >= 2:
        print(count[1])
    else:
        print(count[0])
    print(number_list[-1] - number_list[0])
