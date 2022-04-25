# fail
import sys

n = int(sys.stdin.readline())
inputArray = list(map(int, sys.stdin.readline().split()))

def long_array(array, n):
    longArray = [[] for _ in range(n)]
    
    for i in range(n):
        longArray.append([inputArray[i], inputArray[i], 1])
    
    for i in range(1, n):
        for j in range(0, n - i):
            temp = [0, 0, 1]
            for k in range(1, i):
                print(inputArray)
                print(longArray)
                leftbigg = longArray[k][j][1] 
                rightsmall = longArray[i - k][j + k][0]
                if leftbigg < rightsmall:
                    temp[0] = (longArray[k][j][0])
                    temp[1] = (longArray[i - k][j + k][1])
                    temp[2] = (longArray[k][j][2] + longArray[i - k][j + k][2])
                else:
                    if longArray[k][j][2] > longArray[i - k][j + k][2]:
                        temp[0] = (longArray[k][j][0])
                        temp[1] = (longArray[k][j][1])
                        temp[2] = (longArray[k][j][2])
                    else:
                        temp[0] = (longArray[i - k][j + k][0])
                        temp[1] = (longArray[i - k][j + k][1])
                        temp[2] = (longArray[i - k][j + k][2])

                if longArray[i][j][2] < temp[2]:
                    longArray[i][j][0] = temp[0]
                    longArray[i][j][1] = temp[1]
                    longArray[i][j][2] = temp[2]

                print(temp)
                print(longArray)

print(long_array(inputArray, n))

# fail
# import sys

# n = int(sys.stdin.readline())
# inputArray = list(map(int, sys.stdin.readline().split()))

# def long_array(array, n):
#     longArray = [[] for _ in range(n)]
#     for i in range(n):
#         longArray[i].append(array[i])
#     maximum = 1
#     for outi in range(0, n):
#         for i in range(outi + 1, n):
#             if longArray[outi][len(longArray[outi]) - 1] < array[i]:
#                 longArray[outi].append(array[i])
#             else:
#                 continue
#         if maximum < len(longArray[outi]):
#             maximum = len(longArray[outi])
#     return maximum

# print(long_array(inputArray, n))
