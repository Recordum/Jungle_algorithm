

def test_object_reference(i,visited, depth):
    if visited[i] == True:
        return

    visited[i] = True

    for i in range(4):
        test_object_reference(i,visited.copy(), depth+1)

    return

if __name__ == '__main__':
    visited = [False]*4

    test_object_reference(0, visited.copy(), 0)

    print(visited)