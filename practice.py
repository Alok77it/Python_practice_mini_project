def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers =  [10,20,471,2912,39]
target = 20

result = linear_search(numbers, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
    