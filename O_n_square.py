def find_duplicate(num):
    for i in range(len(num)):
        for j in range(len(num)):
            if i!=j and num[i]==num[j]:
                return num[i]
            
    return False

number= [1,2,4,5,6,7,8,11,4,6,7]    

result= find_duplicate(number)

if result:
    print(f"duplicate {result} number found at number array ")

else:
    print("not duplicate number are found")    

#Complexity is O(n2) and use is nested loop
# when data / work is increase then operation /work is duble 
# this is why nested loop is often slower  