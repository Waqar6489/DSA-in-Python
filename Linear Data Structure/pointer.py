# arr=[1,3,4,5,6,8,9] # target number sum of 9 like any sum two number of arry =9
# make sure array is must be sorted
# def pointer(num,target):
#     left= 0   #0
#     right= len(num)-1 #6
#     while left < right:
#         total= num[left]+ num[right]

#         if total == target:
#             return [num[left],num[right]], print(left,right)
            
            
#         elif total> target:
#             right = right-1
            
#         else:
#             left= left-1
           
#     return[]

# arr=[1,3,5,6,8,11] 
# print(pointer(arr,14))  


# def reverse(arr):
#     left = 0
#     right = len(arr)-1
#     while right > left:
#        arr[left],arr[right] = arr[right],arr[left]
#        left=left+1
#        right= right-1
#     return arr
# arry = [1,2,3,4,5,6,7]
# print(reverse(arry))   

def sum(arr,target):
    left = 0
    for right in range(1,len(arr)):
       result = arr[left]+arr[right]
       if result==target:
         return [arr[left],arr[right]]
       elif left == len(arr)-2 and right == len(arr) - 1:
          if result==target:
            return [arr[left],arr[right]]
          else:
             return f"Not found pair in {arry} array"   
       else:
          left = left+1  
          right = right+1  
    return [arr[left],arr[right]]
arry = [1,2,3,4,5,6,7]
print(sum(arry,3))

