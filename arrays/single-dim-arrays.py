from array import array

# 1. Create an array and traverse. 
my_array = array('i',[1,2,3,4,5])

print("Array traversal")
for i in my_array:
    print(i)

# 2. Access individual elements through indexes
print("Array access by index")
print(my_array[3])

# 3. Append any value to the array using append() method
print("Array append to another array")
my_array.append(6)
print(my_array)

# 4. Insert value in an array using insert() method.
# Value is inserted at (index-1) position. i.e before index, NOT AT INDEX!
print("Insert element at index")
my_array.insert(3, 11)
print(my_array)

# 5. Extend python array using extend() method
print("Append elements at end of array")
my_array1 = array('i', [10,11,12])
my_array.extend(my_array1)
print(my_array)

# 6. Add items from list into array using fromlist() method
print("Append items to array from a list")
tempList = [20,21,22]
my_array.fromlist(tempList)
print(my_array)

# 7. Remove any array element using remove() method
# Removes by first ocurrence of value. not index!
print("Remove an array by value")
my_array.remove(11)
print(my_array)

# 8. Remove last array element using pop() method
print("Remove last item in array using pop")
my_array.pop()
print(my_array)

# 9. Fetch the index where a value is located. FIRST OCURRENCE
print("Find index of value")
print(my_array.index(21))

# 10. Reverse a python array using reverse() method
print("Reverse an array")
my_array.reverse()
print(my_array)

# Buffer info - tuple of mem location, count of items
print("Show array buffer info")
print(my_array.buffer_info())

# 12. Check for number of occurrences of an element using count() method
print("Count number of ocurrences of a value")
my_array.append(11)
my_array.append(11)
print(my_array.count(11))
print(my_array)

# 14. Convert array to a python list with same elements using tolist() method
print("Convert array to list object")
print(my_array)
print(my_array.tolist())

# 16. Slice Elements from an array.[m:n] Inclusive of m and n
print("Slice array - dump all elements")
cut = len(my_array) - 3 # get last 3 elements
print(my_array[cut:])