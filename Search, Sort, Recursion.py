#Includes
import math

#Binary search
def binary_search(array, target):
    left_index = 0
    right_index = len(array) - 1
    
    while(left_index <= right_index):       #Pag sumobra, imposible n so end
        middle_index = math.ceil((left_index + right_index) / 2)
        
        if target < array[middle_index]:
            right_index = middle_index - 1
        elif target > array[middle_index]:
            left_index = middle_index + 1
        else:
            return middle_index
    
    return None

#Selection sort
def selection_sort(array):
    #sorted_pointer = 0      #Index
    #scan_pointer = 0
    
    for i in range(len(array)):
        minimum = i
        
        for j in range(i+1, len(array)):
            if array[j] < array[minimum]:
                minimum = j
        if i != minimum:
            array[i], array[minimum] = array[minimum], array[i]
    
    return array        #When swapping, use indices? (can both get index and value...)
    
    """
    for i in range(len(array)):
        minimum = array[i]
        
        for j in array[i+1:]:
            if j < minimum:
                minimum = j
        
        if minimum != array[i]:
            array[i], minimum = minimum, array[i]       #This part won't swap list elements?, use indices
        
    return array
    """
    
#Bubble sort
def bubble_sort(array):
    max_index = len(array)
    
    for _ in range(len(array)):             #Like counter
        for j in range(0, max_index-1):
            first = j
            second = j+1
            if array[second] < array[first]:
                array[first], array[second] = array[second], array[first]
        max_index -= 1
    
    return array

#Insertion sort
def insertion_sort(array):
    for i in range(len(array)-1):
        first = i
        second = i+1
        while array[second] < array[first]:
            array[first], array[second] = array[second], array[first]
            first -= 1
            second -= 1
    
    return array

#Merge sort- 2 functions
def merge_sort(array):      #Divides array til size is 1
    #Base case
    if len(array) == 1:
        return array
    else:
        first_half = merge_sort(array[: math.floor(len(array) / 2) ])       #Less #elements
        second_half = merge_sort(array[math.floor(len(array) / 2) :])
    
    return merge(first_half, second_half)       #Calls in else statement must be returned first....

def merge(array1, array2):
    array_result = []
    while (len(array1) != 0 and len(array2) != 0):
        if(array1[0] <= array2[0]):
            array_result.append(array1[0])
            array1.remove(array1[0])
        else:
            array_result.append(array2[0])
            array2.remove(array2[0])
    
    if len(array1) != 0:
        array_result += array1
        array1=[]                   #.clear()- list becomes None, be careful
    if len(array2) != 0:
        array_result += array2
        array2=[]
        
    return array_result
    
#Quick sort
"""
def quick_sort(array):
    #Base case
    if len(array) <= 1:     #Already sorted
        return array
    
    #array_prepared, pivot_idx = median_of_three(array)
    #pivot = array_prepared[pivot_idx]
    #array_prepared[pivot_idx], array_prepared[-1] = array_prepared[-1], array_prepared[pivot_idx]
    pivot = array[-1]
    itemFromLeft_idx = 0        #Larger
    itemFromRight_idx = 0
    #itemFromRight_idx = len(array_prepared)-2
    new_pivot_idx = itemFromLeft_idx
    flag1 = True
    flag2 = True
    
    for i in range(len(array)-1):
        if array[i] > pivot and flag1:
            itemFromLeft_idx = i
            flag1 = False
        if array[:-1][::-1][i] < pivot and flag2:           #[::-1] instead of .reverse()
           itemFromRight_idx = len(array)-2-i               #-2- since original array was referenced...
           flag2 = False
        #if array_prepared[i] < pivot and flag2:
        #    itemFromRight_idx = i
        #    flag2 = False
        if itemFromLeft_idx < itemFromRight_idx and not flag1 and not flag2:
            array[itemFromLeft_idx], array[itemFromRight_idx] = array[itemFromRight_idx], array[itemFromLeft_idx]
            flag1 = True
            flag2 = True
        elif itemFromLeft_idx >= itemFromRight_idx and not flag1 and not flag2:
            break
    new_pivot_idx = itemFromLeft_idx
    array[new_pivot_idx], array[-1] = array[-1], array[new_pivot_idx]
    
    #Recursive call
    left = quick_sort(array[:new_pivot_idx])
    right = quick_sort(array[new_pivot_idx+1:])
    
    #return array, array_prepared[itemFromLeft_idx], array_prepared[itemFromRight_idx], pivot
    return left + [array[new_pivot_idx]] + right

def median_of_three(array):    
    first = array[0]
    last = array[-1]
    mid_index = math.floor(len(array)/2)
    mid = array[mid_index]
    
    if first <= mid and first <= last:
        array[0] = first
        if mid < last:
            array[mid_index] = mid
        else:
            array[mid_index] = last
            array[-1] = mid
    elif mid <= first and mid <= last:
        array[0] = mid
        if first < last:
            array[mid_index] = first
        else:
            array[mid_index] = last
            array[-1] = first
    else:
        array[0] = last
        if first < mid:
            array[mid_index] = first
            array[-1] = mid
        else:
            array[mid_index] = mid
            array[-1] = first
    
    #array[mid_index], array[-1] = array[-1], array[mid_index]
    return array, mid_index
"""

def quick_sort(array):
    #Base case
    if len(array) <= 1:
        return array
    
    #Set pivot at end of array, goal: find final place of pivot
    pivot = array[-1]
    
    #2 indices
    j = 0       #Start of array
    i = -1      #Start 1 less than j?
    
    #Temp variable for swap
    #Check if value at j is less than pivot- i++ then swap i and j, else j++; repeat til j reaches pivot
    #Final place of j is at i+1, elements at left of pivot < and at right >, not yet ordered
    for j in range(len(array)):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    i+=1
    array[i], array[-1] = array[-1], array[i]
    
    #Create 2 partitions- left- :pivot (pivot not included), right pivot (not included):
    left = quick_sort(array[:i])
    right = quick_sort(array[i+1:])
    
    #return array, pivot
    return left + [array[i]] + right

#Recursion
#Factorial
def factorial_recursive(n):     #+int
    #Base case
    if n==0 or n==1:
        return 1
    else:
        n = n * factorial_recursive(n-1)
    
    return n
    
def factorial_iterative(n):
    answer = 1
    if n==0 or n==1:
        return 1
    else:
        for i in range(1, n+1):
            answer *= i
        return answer
    
#Fibonacci
def fibonacci_recursive(n):
    #Base case
    if n==1 or n==2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    #O(n^2), memoization to improve

def fibonacci_iterative(n):
    first_term = 1
    second_term = 1
    next_term = 0
    
    for _ in range(n-2):
        next_term = first_term + second_term
        first_term = second_term
        second_term = next_term
    
    return next_term


### Main ###
array = [1, 2, 3, 4, 5, 6, 7, 8]
array1 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0, 10]
array_test_1 = [10, 7, 14, 3, 8, 5, 19, 1, 13, 4, 11, 6, 18, 2, 15, 20, 9, 17, 12, 16]
array_test_2 = [5, 12, 8, 19, 14, 2, 3, 9, 17, 1, 16, 6, 11, 7, 10, 20, 4, 13, 18, 15]
array_expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
target = 8

#bin_search = binary_search(array, target)
#Find index of target in array
#print(bin_search)

"""
if selection_sort(array_test_1) == array_expected:
    print("Correct")
else:
    print("Incorrect")
if selection_sort(array_test_2) == array_expected:
    print("Correct")
else:
    print("Incorrect")
    
if bubble_sort(array_test_1) == array_expected:
    print("Correct")
else:
    print("Incorrect")
if bubble_sort(array_test_2) == array_expected:
    print("Correct")
else:
    print("Incorrect")

if insertion_sort(array_test_1) == array_expected:
    print("Correct")
else:
    print("Incorrect")
if insertion_sort(array_test_2) == array_expected:
    print("Correct")
else:
    print("Incorrect")
    
if merge_sort(array_test_1) == array_expected:
    print("Correct")
else:
    print("Incorrect")
if merge_sort(array_test_2) == array_expected:
    print("Correct")
else:
    print("Incorrect")
    
if quick_sort(array_test_1) == array_expected:
    print("Correct")
else:
    print("Incorrect")
if quick_sort(array_test_2) == array_expected:
    print("Correct")
else:
    print("Incorrect")
"""
    
# print(factorial_recursive(4))
# print(factorial_iterative(4))
# print(fibonacci_recursive(20))
# print(fibonacci_iterative(20))