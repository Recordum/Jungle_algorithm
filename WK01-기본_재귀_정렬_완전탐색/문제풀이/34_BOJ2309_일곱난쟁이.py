import sys
input = sys.stdin.readline

def is_true(heights):
    for i in range(len(heights)):
        for j in range(i+1, len(heights)):
            result = sum(heights) - heights[i] - heights[j]

            if result == 100:
                fake_height_1 = heights[i]
                fake_height_2 = heights[j]
                heights.remove(fake_height_1)
                heights.remove(fake_height_2)

                return heights

heights = [0]*9

for i in range(9):
    inp = int(input())
    heights[i] = inp

result = is_true(heights)
sorted_result = sorted(result)
for res in sorted_result:
    print(res)



