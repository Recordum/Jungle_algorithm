import sys
from collections import deque
input = sys.stdin.readline

def copy(display):
    return display

def paste(display, clipboard):
    return display + clipboard
def delete(display):
    display -= 1
    return display

def generate_emoticion(display, clipboard):
    global n 
    q = deque([])
    q.append([display, clipboard, 0])

    while(q):
        display, clipboard, count = q.popleft()
        if display == n:
            return count
        for i in range(3):
            if i == 0:
                new_clipboard = copy(display)
                new_display = display
            if i == 1 and clipboard:
                new_display = paste(display, clipboard)
                new_clipboard = clipboard
            if i == 2 and display:
                new_display = delete(display)
                new_clipboard = clipboard

            if not visited[new_display][new_clipboard]:
                visited[new_display][new_clipboard] = True
                q.append([new_display, new_clipboard, count + 1])
            
        


n = int(input())
visited = [[False] * 10000 for _ in range(10000)]
visited[1][0] = True
clipboard = 0
display = 1
print(generate_emoticion(display=1, clipboard=0))

