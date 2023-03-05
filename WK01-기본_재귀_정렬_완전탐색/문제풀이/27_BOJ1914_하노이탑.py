import sys
input = sys.stdin.readline
def recursive_move(number, start, goal):
    if number == 1:
        print(str(start) + " " + str(goal))
        return

    recursive_move(number - 1, start, 6-start-goal)
    print(str(start) + " " + str(goal))
    recursive_move(number - 1, 6-start-goal, goal)


if __name__ == '__main__':
    n = int(input())
    hanoi_route = []
    print(2**n-1)
    if n < 21 :
        recursive_move(n,1,3)



