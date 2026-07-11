       
# def arr(a):        
#  large= a[0]
#  index= 0
#  for i in range(len(a)):
#     if a[i] > large:
#         large = a[i]
#         index=i
#  return f"max number is {large} and index is {index}"        
# a= [100,13,400,6,12,8,9,9]
        
# print(arr(a)) 

def FindSortedOrNot(a):
    # Loop up to len(a) - 1 so i + 1 doesn't go out of bounds
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return "array is not sorted" # Found a disorder, exit early
            
    return "array is sorted" # Looked at all pairs, everything is fine

a = [1, 3, 4, 6, 7, 8, 9, 10] 
print(FindSortedOrNot(a))

# def findSecLarge(a):
#     large= a[0]
#     seclarge=a[0]
#     for i in a:
#         if i> large:
#             seclarge=large
#             large = i
#         elif i > seclarge:
#             seclarge=i
#     return seclarge
# a = [1, 3, 4, 6, 7, 8, 9, 11,10]     
# print(findSecLarge(a))    
                

        
    
        
        


                