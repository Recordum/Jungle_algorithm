def div_recursion(length, new_row , new_columm, r, c, number):
    if length == 1:
        return int(number)
    if r < length/2 + new_row and c < length/2 + new_columm:
        return div_recursion(length / 2, new_row , new_columm, r, c, number)
    if r < length/2 + new_row and c >= length/2 + new_columm:
        return div_recursion(length / 2, new_row , new_columm + length/2, r, c, number + (length / 2) ** 2)
    if r >= length/2 + new_row and c < length/2 + new_columm:
        return div_recursion(length / 2, new_row + length/2, new_columm,r, c, number + (length / 2) ** 2 * 2)
    if r >= length/2 + new_row and c >= length/2 + new_columm:
        return div_recursion(length / 2, new_row + length/2, new_columm + length/2, r, c, number + (length / 2) ** 2 * 3)


n, r, c = map(int, input().split())
count = 0

length = 2 ** n

print(div_recursion(length,0,0, r, c, 0))



