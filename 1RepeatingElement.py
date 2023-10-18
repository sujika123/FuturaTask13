# Program to find the first repeating element in array of integers
#method : 1
def printFirstRepeating(arr, n):
    # Initialize index of first repeating element
    Min = -1

    # Creates an empty hashset
    myset = dict()

    # Traverse the input array from right to left
    for i in range(n - 1, -1, -1):

        # If element is already in hash set,
        # update Min
        if arr[i] in myset.keys():
            Min = i

        else:  # Else add element to hash set
            myset[arr[i]] = 1

    # Print the result
    if (Min != -1):
        print("The first repeating element is",
              arr[Min])
    else:
        print("There are no repeating elements")


# Driver Code
arr = [10, 5, 3, 4, 3, 5, 6]

n = len(arr)
printFirstRepeating(arr, n)


print("_______________________________")
# ___________________________________________

# Method 2:

arr = [1, 3, 4, 5, 5, 3, 4, 6]

repeat_ele = -1

# sorting the array
arr.sort()

for i in range(len(arr) - 1):
    # check if adjacent elements are equal or not
    if arr[i] == arr[i + 1]:
        repeat_ele = arr[i]
        break

# if repeat_ele is -1 means there are no repeating elements
if repeat_ele == -1:
    print("There are no repeating elements in array")
else:
    print("The first repeating element is", repeat_ele)

print("________________________")
# Method 3
arr = [1,3,4,4,5,3,4,6]
rpt_ele = -1

for element in arr:
    c = arr.count(element)
    if c > 1:
        rpt_ele = element
        break

if rpt_ele == -1:
    print("There are no repeating elements in array")
else:
    print("The first repeating element is", rpt_ele)