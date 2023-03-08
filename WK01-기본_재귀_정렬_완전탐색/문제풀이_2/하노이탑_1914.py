import sys
input = sys.stdin.readline


def recursive_move(n, start, goal):
    if n == 1:
        print(str(start) + " " + str(goal))
        return

    recursive_move(n-1, start, 6-start-goal)
    print(str(start) + " " + str(goal))
    recursive_move(n-1, 6-start-goal, goal)




n = int(input())
print(2**n-1)
if n < 21 :
    recursive_move(n,1,3)
