def solution(s):
    answer = 0
    index = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    translation = dict()
    translation['zero'] = 0
    translation['one'] = 1
    translation['two'] = 2
    translation['three'] = 3
    translation['four'] = 4
    translation['five'] = 5
    translation['six'] = 6
    translation['seven'] = 7
    translation['eight'] = 8
    translation['nine'] = 9

    check_str = ''
    for i in range(len(index)):
        s = s.replace(index[i], str(translation[index[i]]))
    answer = int(s)
    return answer