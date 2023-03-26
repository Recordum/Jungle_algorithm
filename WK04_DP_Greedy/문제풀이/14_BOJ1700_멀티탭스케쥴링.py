import sys
input = sys.stdin.readline

n, k = map(int, input().split())
used_order = list(map(int, input().split()))
used = []
count = 0
for i in range(len(used_order)):
    if used_order[i] in used:
        continue
    if len(used) < n:
        used.append(used_order[i])
        continue
    if len(used) == n:
        check_plug = []
        remove_candidate = list(map(int,used))
        for j in range(i + 1, len(used_order)):
            check_plug.append(used_order[j])
        for plug in check_plug:
            if plug in remove_candidate:
                if len(remove_candidate) == 1:
                    break
                remove_candidate.remove(plug)
        used.remove(remove_candidate[0])
        used.append(used_order[i])
        count += 1
print(count)