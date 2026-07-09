#The enumerate() function tracks both the index and the value during the loop.

def linear(name, target):
    for index, i in enumerate(name):
      if i == target:
        return index
    return -1

name_arr= ["waqar","ali","hamza","ahmad","zeeshan","hamid","taha","ammar","abu huraira"]
target_name= "abu huraira"
result= linear(name_arr,target_name)
if result !=-1:
    print(f"name is found and index is {result}")
else:
    print("name is not found")   


# complexity O(n) increase work when data increase


def find_large_num(arr):
   large = arr[0]
   for i in range(1, len(arr)):
      if arr[i] > large:
         large = arr[i]
   return large  

array= [1,3,5,3,0,8,9,7,30]  
print(find_large_num(array))
