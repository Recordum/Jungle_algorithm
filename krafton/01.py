# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, C):
    # Implement your solution here
    col_stack = []
    table = [[]]
    comma_count = 0
    find_index = 0
    row_count = 0
    find_list = []
    for i in range(len(S)):
        if S[i] == ',':
            table[row_count].append("".join(col_stack))
            col_stack = []
            if table[row_count][comma_count] == C and row_count == 0:
                find_index = comma_count
            if comma_count == find_index and row_count != 0:
                find_list.append(table[row_count][comma_count])
            comma_count += 1
            continue
        if S[i] == '\n':
            table[row_count].append("".join(col_stack))
            col_stack = []
            if table[row_count][comma_count] == C and row_count == 0:
                find_index = comma_count
            if comma_count == find_index and row_count != 0:
                find_list.append(table[row_count][comma_count])
            row_count += 1
            table.append([])
            comma_count = 0
            continue
        col_stack.append(S[i])
        if i == len(S) - 1:
            table[row_count].append("".join(col_stack))
            col_stack = []
            if comma_count == find_index and row_count != 0:
                find_list.append(table[row_count][comma_count])
    integer_list = list(map(int, find_list))
    integer_list.sort()
    return integer_list[-1]


print(solution("area,temp2,temp\nCN,1,-3\nUSA,4,-4\ntoky,4,-2", "temp"))
print(type(solution("area,temp2,temp\nCN,1,-3\nUSA,4,-4\ntoky,4,-2", "temp")))
