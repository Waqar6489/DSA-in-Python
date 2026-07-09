# linear search complexity is O(n) like search item one by one in arry
# not required for sorted arry 

def Linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i ]== target:
            return f"Found {target} number in {i} index"
       
    return f"Not found {target} number in this {arr} array"
        
   
array=[1,2,4,5,6,7,7,9,10,11]
print(Linear_search(array,1))
