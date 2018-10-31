# Coding problem of the day: Day 2
# Given an array of integers, return a new array such that each element at
# index i of the new array is the product of all the numbers in the original array except the one at i.
# Example  if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]

def productiveArray(list):
    newList = []
    for i in range(0,len(list)):
        # Reset product after interating through list
        product = 1
        # Going through list and looking at every position ignoring index i
        for j in list[0:i]:
            product *= j
        for j in list[i+1:len(list)]:
            product *= j
        newList.append(product)
    return newList

#Tests
print(productiveArray([1,2,3,4,5]))
print(productiveArray([1,2,3]))
