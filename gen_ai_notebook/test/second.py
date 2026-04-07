

#2. Remove duplicates from a list while preserving order
print("\n\n #2. Remove duplicates from a list while preserving order\n")
lst = [1, 2, 2, 3, 4, 4, 1, 5]

result = set(lst)

print(result)

result = []

for i in lst:
    if i not in result:
        result.append(i)

print(result)


print("\n\n 3.Reverse an array in place without using extra space.\n")

arr = [1, 2, 3, 4, 5, 6]

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

result = (arr[k+1:])

for i in range(0,len(arr)-k):
    result.append(arr[i])

print(result)


print("5. Find the intersection of two lists")
list1 = [1, 2, 3, 4, 4, 5]
list2 = [3, 4, 6, 7]

# Output: [3, 4]
result = []
for i in list2:
    if i in list1:
        result.append(i)

print(result)

print("6. Move all zeroes to the end of a list without changing order of non-zero elements")
lst = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
zero = []
for i in lst:
    if i is 0:
        zero.append(i)
        lst.remove(i)
lst = lst+zero
print(lst)


print("7. Find the second largest element in a list")

lst = [10, 20, 4, 45, 45, 99, 99]

 # Output: 45

large = -2
large2 = -1

for i in lst:
    if i > large:
        large2 = large
        large = i

print(large)
print(large2)



print("10. Count the frequency of each element in a list")

lst = [1, 2, 2, 3, 3, 3, 4,4]

set1 = set(lst)
list1 = {}
touple = ()

for i in set1:
    list1[i] = lst.count(i)
    touple += (i,lst.count(i))

print(list1)
print(touple)