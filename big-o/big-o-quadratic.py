intArray = [1, 2, 3, 4, 5]
stringArray = ["one", "two", "three", "four", "five", "six", "seven", "eight"]

print('######  Quadratic time complexity O(n*n) #######')
for x in intArray:
    for y in stringArray:
        print(x, y)