# binary search algo complexity is O(logn)
# Array must be sorted if array is not sorted then wrong output
# Binary search fast way to find output

def Binary_search(arr,target):
    left = 0
    right = len(arr) -1
    while right >= left:
        middle= (left + right) //2
        if arr[middle] == target:
            return f"Found {target} number in {middle} index"
        elif arr[middle]<target:
             left = middle + 1
        else:
             right= middle - 1
    return "Not found"
array=[1,2,3,4,5,6,7,8,9] 
print(Binary_search(array,10))   