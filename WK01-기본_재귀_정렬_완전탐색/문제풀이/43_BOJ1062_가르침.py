import sys
input = sys.stdin.readline

def dfs_teach(k, index):
    global result

    if k == 0:
        result_count = 0
        for word in words:
            is_teaching_word = True
            for spell in word:
                if learned_spell_list[ord(spell) - 97] == 0:
                    is_teaching_word = False
                    break
            if is_teaching_word:
                result_count += 1

        result = max(result, result_count)
        return

    for i in range(index, len(learned_spell_list)):
        if learned_spell_list[i] == 0:
            learned_spell_list[i] = 1
            dfs_teach(k-1, i)
            learned_spell_list[i] = 0
    return



n, k = map(int, input().split())
result = 0
words = [input().rstrip()[4:-4] for _ in range(n)]

if k < 5:
    print(0)
    exit()
elif k == 26:
    print(n)
    exit()

learned_spell_list = [0] * 26
for i in ('a','n','t','i','c'):
    learned_spell_list[ord(i) - ord('a')] = 1

dfs_teach(k - 5, 0)
print(result)
