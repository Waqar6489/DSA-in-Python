def find_name(name,target):
    left= 0
    right= len(name)-1
    while left <= right:
        middle= (left+right)//2

        if name[middle] == target:
            return middle
        elif name[middle] < target:
            left = middle + 1
        else:
            right = middle -1

    return -1

name_arr= ["waqar","ali","hamza","ahmad","zeeshan","hamid","mhamid","taha","taha","ammar","abu huraira"]
target_name= "mhamid"

result = find_name(name_arr,target_name)

if result !=-1:
    print(f"{target_name} name is found at {result} index")

else:
    print("name is not found")    


#Complexity is O(logn)    
# use is binary search
# very fast for large sorted data(a,b,c,d,e,f,g,h) or (1,2,3,4,5,6,7,8,9)