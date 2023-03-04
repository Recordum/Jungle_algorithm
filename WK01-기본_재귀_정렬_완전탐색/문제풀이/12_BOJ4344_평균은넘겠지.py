
n = int(input())

results = []

for i in range(n):
    numbers = list(map(int, input().split()))
    count = 0
    add =  sum(numbers) - numbers[0]
    average = add / numbers[0]

    for i in range(1, len(numbers)):
        if average < numbers[i]:
            count += 1
    results.append((count / (len(numbers) -1) * 100))
for result in results:
    print('%.3f' % result +'%')


#     tests.append(list(map(int, input().split())))
#
# for i in range(len(tests)):
#     sum = 0
#     count = 0
#     for j in range(1 ,len(tests[i])):
#         sum = sum + tests[i][j]
#
#     average = sum/(len(tests[i])-1)
#
#     for k in range(len(tests[i])):
#         if average < tests[i][k]:
#             count += 1
#
#     results[i] =(count / (len(tests[i]) - 1) * 100)
#
# for result in results:
#     print('%.3f' % result +'%')
#
#     # if len(result) < 6:
#     #     print(result + "0%")
#     #     continue
#     # print(result + "%")
