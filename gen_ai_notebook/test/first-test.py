print("kapil")


list1 = [2,3,4,5,5,6,78,9]

max1 = -1 
min1 = 999
for i in list1:
    if max1 < i:
        max1 = i
    if min1 > i:
        min1 = i

print(max1,min1)

print(max(list1))
print(min(list1))


#2. Remove duplicates from a list while preserving order
print("\n\n #2. Remove duplicates from a list while preserving order\n")
lst = [1, 2, 2, 3, 4, 4, 1, 5]

seen = set()

result = []

for i in lst:
    if i not in seen:
        seen.add(i)
        result.append(i)

print(result)

print("\n\n 3.Reverse an array in place without using extra space.\n")

arr = [1, 2, 3, 4, 5]

left = 0 
right = len(arr)-1

while left<right:
    arr[left], arr[right] = arr[right], arr[left]
    left +=1
    right -=1

print(arr)


print("\n 4. Rotate an array by k positions to the right (circular rotation)")

arr = [1, 2, 3, 4, 5]
# Output: [4, 5, 1, 2, 3]
print(arr)
k = 2

list1 = (arr[3:])

for i in range(0,len(arr)-k):
    list1.append(arr[i])

print(list1)

print("5. Find the intersection of two lists")
list1 = [1, 2, 3, 4, 4, 5]
list2 = [3, 4, 6, 7]

# Output: [3, 4]
output = []
for i in list1:
    if i in list2 and i not in output:
        output.append(i)

print(output)

print("6. Move all zeroes to the end of a list without changing order of non-zero elements")
lst = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

output = []
zero = []

for i in lst:
    if i == 0:
        zero.append(0)
        lst.remove(i)

lst += zero
print(lst)

print("7. Find the second largest element in a list")

lst = [10, 20, 4, 45, 99]

 # Output: 45

large  = 0
large1 = 0
for i in lst:
    if i> large:
        large1=large
        large=i

print(large1)

print("9. Implement binary search on a sorted list")
def binary_search(arr,target):
    left = 0 
    right = len(arr)-1

    while left<=right:
        mid = (left+right)//2
        if target == arr[mid]:
            return arr[mid]
        elif target > arr[mid]:
            left = mid+1
        else:
            right = mid-1

    return -1

arr = [1, 2, 3, 4, 5, 6]
target = 4
print(binary_search(arr, target)) 

print("10. Count the frequency of each element in a list")

lst = [1, 2, 2, 3, 3, 3, 4,4]

set1 = set(lst)
counter = {}
touple = ()
print(set1)
for i in set1:
    counter[i] = lst.count(i)
    touple += (i,lst.count(i))

print(counter)
print(touple)

print("Check if an array is a palindrome.")
#Input: [1, 2, 3, 2, 1] → Output: True
Input = [1, 2, 3, 2, 1]
output = None

if Input == Input[::-1]:
    print(True)
else:
    print(False)

print("Find the first non-repeating element in an array.")
lst = [4, 5, 1, 2, 0, 4]

for i in lst:
    # print(lst.count(i))
    if lst.count(i) <= 1:
        print(i)
        break

"""
Find the majority element (appears more than n/2 times).
Input: [3, 3, 4, 2, 3, 3, 3] → Output: 3
"""
print("Find the majority element (appears more than n/2 times).")

Input=[3, 3, 4, 2, 3, 3, 3] 
target = len(Input)/2

set1  = set(Input)
for i in set1:
    if Input.count(i) >= target:
        print(i)
        break

"""
Segregate even and odd numbers.
Input: [1, 2, 3, 4, 5] → Output: [2, 4, 1, 3, 5]
"""

Input = [1, 2, 3, 4, 5]

even = []
odd = []

for i in Input:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

output = even
output += odd

print(output)

print("Input: [100, 4, 200, 1, 3, 2] → Output: 4 (1,2,3,4))")

Input = [100, 4, 200, 1, 3, 2] 
Input = sorted(Input)
output = []
prev = Input[0]
output.append(prev)
for i in Input:
    if prev == i-1:
        output.append(i)
        prev = i

print(output)


print("print(count_characters(aabbca))  # {'a':3, 'b':2, 'c':1}")


input = "aabbca"
dis = set(input)
dist1 = {}
for i in dis:
    dist1[i] = input.count(i)
    # print(i)

print(dist1)
print(sorted(dist1.items()))