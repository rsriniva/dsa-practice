# List declaration
things = ["bread","milk","jam"]
print(things)

# add at end of list
things.append("eggs")
print(things)

# Nested Lists
nestedList = ['as',1,'c',2.65, '''ddd''',[1,2,3],[1.1,2.45,1]]
print(nestedList)

# Access by index
print(nestedList[3])

# You can access the list from the end - backward traversal
print(nestedList[-2])

# List membership check using 'in' operator

print('c' in nestedList)

# Traversal
for i in nestedList:
    print(i)


