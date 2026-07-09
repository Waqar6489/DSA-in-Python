# Selection sort
# first Step: find smaller number in unsorted array or other
# Second Step: Swape the front part of unsorted array or other
# Third Step: repeat step

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index= i
#         print(min_index)
#         for j in range(i+1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[min_index], arr[i]  = arr[i], arr[min_index]

#     return arr
# array=[2,4,1,5,6,3,7]
# print(selection_sort(array))  

# n = int(input("enter number : ")) 

# def square(n):
#     for i in range(0,n):
#         print(i ** 2)  # Yields values sequentially instead of exiting

# square(n)          

# def is_leap(year):
#     leap = False 
#     if year%4==0 and year%100!=0 or year%400==0:
#         leap = True    
#     return leap

# year = int(input("enter num "))
# print(is_leap(year))

n = int(input("enter "))
def string(n):
    st = ""
    for i in range(n):
        st += str(i+1)
        
    print(st)
    
string(n)    
#time complexity is O(n^2)
#space complexity is O(1) beacuse this program take time to perform sorting not add new array
