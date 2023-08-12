from collections import defaultdict
 
def table_func(diagram):
    m = len(diagram)
    d = defaultdict(int)
 
    begin = 1
    matched = 0
 
    while begin + matched < m:
        if diagram[begin + matched] == diagram[matched]:
            matched += 1
            d[begin + matched - 1] = matched
        elif matched == 0:
            begin += 1
        else:
            begin += matched - d[matched - 1]
            matched = d[matched - 1]
    return d
 
 
 
def KMP(word, diagram):
    table = table_func(diagram)
    results = []
    p = 0
 
    for idx in range(len(word)):
        while p > 0 and word[idx] != diagram[p]:
            p = table[p - 1]
 
        if word[idx] == diagram[p]:
            if p == len(diagram) - 1:
                results.append(idx - len(diagram) + 2)
                p = table[p]
            else:
                p += 1
 
    return results

def solution(S):
    result = []
    answer = -2
    for i in range(1, len(S)):
        result = KMP(S, S[i - 1] + S[i])
        if len(result) < 2:
            answer = max(answer, -1)
            continue
        answer = max(answer, result[-1] - result[0])
    return answer