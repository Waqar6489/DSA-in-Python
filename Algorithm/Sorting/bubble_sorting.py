def bubble_sort(num):
    lenght = len(num)
    for i in range(lenght): # 0 first iteration and 1 second iteration and so end
        for j in range(0, lenght-i-1): # 0 to 6-0-1= 5 first iteration and # 0 to 6-1-1=4 second iteration
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
                print("swapping", num[j], "and", num[j+1])

    return num

number = [2,3,5,7,1,6]   
print(bubble_sort(number))     

"""
Bubble Sort Implementation
dry run of the bubble sort algorithm on the array [2,3,5,7,1,6]:
1. Start with the first element (2). Compare it with the second element (3).
    - Since 2 is less than 3, they stay in their places. The array remains [2, 3, 5, 7, 1, 6].
2. Move to the second element (3). Compare it with the third element (5).
    - Since 3 is less than 5, they stay in their places. The array remains [2, 3, 5, 7, 1, 6].
3. Move to the third element (5). Compare it with the fourth element (7).
    - Since 5 is less than 7, they stay in their places. The array remains [2, 3, 5, 7, 1, 6].
4. Move to the fourth element (7). Compare it with the fifth element (1).
    - Since 7 is greater than 1, they swap places. The array becomes [2, 3, 5, 1, 7, 6].
5. Move to the fifth element (7). Compare it with the sixth element (6).
    - Since 7 is greater than 6, they swap places. The array becomes [2, 3, 5, 1, 6, 7].
6. Repeat the process for the remaining elements until the entire array is sorted.    
"""

#time complexity is O(n^2)
#space complexity is O(1) beacuse this program take time to perform sorting not add new array
# sort aaray to small to large or large to small
# in bubble sort, compare neighbour number like [0 index to 1 index]