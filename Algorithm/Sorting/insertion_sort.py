array=[3,7,2,1]

def insertion_sort(array):
    for i in range(1,len(array)):
        current = array[i]
        j= i-1
        while j>=0 and array[j]>current: 
            array[j+1]=array[j]
            j-=1
        array[j+1]=current
    return array

print(insertion_sort(array))          

"""
dry run of the insertion sort algorithm on the array [3,7,2,1]:
1. Start with the second element (7). Compare it with the first element (3).
    - Since 7 is greater than 3, it stays in its place. The array remains [3, 7, 2, 1].
2. Move to the third element (2). Compare it with the elements to its left.
    - 2 is less than 7, so it moves to the left. The array becomes [3, 2, 7, 1].
    - 2 is greater than 3, so it stays in its place. The array remains [2, 3, 7, 1].
3. Move to the fourth element (1). Compare it with the elements to its left.
    - 1 is less than 7, so it moves to the left. The array becomes [2, 3, 1, 7].
    - 1 is less than 3, so it moves to the left. The array becomes [2, 1, 3, 7].
    - 1 is less than 2, so it moves to the left. The array becomes [1, 2, 3, 7].
4. The array is now sorted: [1, 2, 3, 7].
"""
# Time Complexity: O(n^2) in the worst case, where n is the number of elements in the array. This occurs when the array is sorted in reverse order.
# Time Complexity: O(n) in the best case, where n is the number of elements in the array. This occurs when the array is already sorted.
# Time Complexity: O(n^2) in the average case, where n is the number of elements in the array. This occurs when the array is randomly ordered.
# Space Complexity: O(1) since we are sorting the array in place and not using any additional data structures.

"""
Write insertion sort algorithm.
First, we start with the second element of the array and compare it with the elements before it. If the current element is smaller than the previous elements, we shift those elements to the right to make space for the current element. We repeat this process for each element in the array until the entire array is sorted.
"""
