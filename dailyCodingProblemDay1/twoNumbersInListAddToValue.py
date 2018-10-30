# Given a list of numbers and a number k, return whether any two numbers
# from the list add up to kself.

# Example given[10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17

def twoNums (list, k):
    for i in range(0, len(list) - 1):
        for j in range(0, len(list)):
            if (list[i] + list[j] == k):
                return True
    return False

#Returns True
print(twoNums([10,15,3,7], 17))

#Returns False
print(twoNums([10,15,3,7], 16))
