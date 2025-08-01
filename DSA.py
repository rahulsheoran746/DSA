# # next smaller element
# arr = [2, 1, 4, 3]
# def next_smaller_element(arr):
#     n = len(arr)
#     lst = [-1] * n
#     stack = [-1]
#     for i in range(n-1, -1, -1):
#         while stack and stack[-1] >= arr[i]:
#             stack.pop()
#         if stack:
#             lst[i] = stack[-1]
#         stack.append(arr[i])

#     return lst

# # ans = next_smaller_element(arr)
# def brute_force(arr):
#     ans_lst = [-1] * len(arr)
#     for i in range(len(arr) - 1):
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[i]:
#                 ans_lst[i] = arr[j]
#                 break
#     return ans_lst 

# ans = brute_force(arr)
# print(ans)

# # previous smaller element
# arr = [2, 1, 4, 3]
# def prevSmallerElement(arr):
#     n = len(arr)
#     stack = [-1]
#     lst = [-1] * n
#     for i in range(n):
#         while stack and stack[-1] >= arr[i]:
#             stack.pop()
#         if stack:
#             lst[i] = stack[-1]
#         stack.append(arr[i])
#     return lst

# ans = prevSmallerElement(arr)
# print(ans)

# # maximum element in an array for each range
# arr = [6, 2, 4, 1]
# map = {}
# for i in range(len(arr)):
#     map[(i, i)] = arr[i]
#     for j in range(i + 1, len(arr), 1):
#         map[(i, j)] = max(arr[j], map[(i, j - 1)])

# print(map)

# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         print('maximum element from range',i,' to ',j,' is' , map[(i, j)])

# #prev greater element
# arr = [2, 1, 4, 3]
# def prev_greater_number(arr):
#     n = len(arr)
#     lst = [-1] * n
#     stack = []
#     for i in range(n):
#         while stack and stack[-1] <= arr[i]:
#             stack.pop()
#         if stack:
#             lst[i] = stack[-1]
#         stack.append(arr[i])
#     return lst
# ans = prev_greater_number(arr)
# print(ans)

# # next greater element
# arr = [2, 1, 4, 5]

# def next_greater_element(arr):
#     n = len(arr)
#     lst = [-1] * n
#     stack = []
#     for i in range(n-1, -1, -1):
#         while stack and stack[-1] <= arr[i]:
#             stack.pop()
#         if stack:
#             lst[i] = stack[-1]
#         stack.append(arr[i])
#     return lst 
# ans = next_greater_element(arr)
# print(ans)

# # next greater element with index 
# arr = [2, 1, 4, 5]

# def next_greater_element(arr):
#     n = len(arr)
#     lst = [-1] * n
#     stack = []
#     for i in range(n-1, -1, -1):
#         while stack and arr[stack[-1]] <= arr[i]:
#             stack.pop()
#         if stack:
#             lst[i] = arr[stack[-1]]
#         stack.append(i)
#     return lst 
# ans = next_greater_element(arr)
# print(ans)

# # next smaller element with index 
# arr = [2, 1, 4, 0]

# def next_smaller_element(arr):
#     n = len(arr)
#     lst = [-1] * n
#     stack = []
#     for i in range(n-1, -1, -1):
#         while stack and arr[stack[-1]] >= arr[i]:
#             stack.pop()
#         if stack:
#             lst[i] = arr[stack[-1]]
#         stack.append(i)
#     return lst
# ans = next_smaller_element(arr)
# print(ans)

# heights = [2,1,5,6,2,3]
# def largest_rectangle_area(heights):
#     print(heights)
#     n = len(heights)
#     print(n)
#     max_area = 0
#     for i in range(n):
#         length = heights[i]
#         width = 1
#         j = i - 1
#         while j >= 0 and heights[j] >= length:
#             width += 1
#             j-=1
#         j = i + 1
#         while j < n and heights[j] >= length:
#             width += 1
#             j +=1
#         area = length * width
#         print(f'Area for height at index {i} is: {area}')
#         max_area = max(max_area, area)

#     return max_area

# largest rectangle area from histogram
# def nextSmallerElement(heights):
#     n = len(heights)
#     lst = [-1] * n
#     stack= []
#     for i in range(n - 1, -1, -1):
#         while stack and heights[stack[-1]] >= heights[i]:
#             stack.pop()
#         if stack:
#             lst[i] = stack[-1]
#         stack.append(i)
#     return lst

# def prevSmallerElement(heights):
#     n = len(heights)
#     lst = [-1] * n
#     stack= []
#     for i in range(n):
#         while stack and heights[stack[-1]] >= heights[i]:
#             stack.pop()
#         if stack:
#             lst[i] = stack[-1]
#         stack.append(i)
#     return lst

# def largest_rectangle_area(heights):
#     n = len(heights)
#     next = nextSmallerElement(heights)
#     prev = prevSmallerElement(heights)
#     max_area = float('-inf')
#     for i in range(n):
#         length = heights[i]
#         if next[i] == -1 :
#             next[i] = n
#         width = next[i] - prev[i] - 1
#         area = length * width
#         max_area = max(max_area, area)
#     return max_area

# ans = largest_rectangle_area(heights)
# print(ans)

# squares = []
# for x in range(10):
#     squares.append(x**2)
# print(x)
# print(x + 1)
# print(squares)


# # #print permutations of a string

# str = 'abc'
# def solveRec(str, ans, temp):
#     if len(str) == 0:
#         ans.append(temp)
#         return
#     for i in range(len(str)):
#         currchar = str[i]
#         remainingStr = str[ : i] + str[i + 1 :]
#         solveRec(remainingStr, ans, temp + currchar)
    
# def printPermutations(str):
#     ans = []
#     solveRec(str, ans, '')
#     return ans
# print(printPermutations(str))


# # Heap Data Structure
# class Heap:
#     def __init__(self):
#         self.arr = []
#         self.size = 0

#     def insert(self, value):
#         # steps
#         # append value ot last of array
#         # increase size of array by 1
#         # call heapify_up with last index 
#         self.arr.append(value)
#         self.size += 1
#         self.heapify_up(self.size - 1)
    
#     def heapify_up(self, index):
#         parent_index = (index - 1)//2
#         if index > 0 and self.arr[parent_index] < self.arr[index]:
#             self.arr[parent_index] , self.arr[index] = self.arr[index], self.arr[parent_index]
#             self.heapify_up(parent_index)

#     def insert_at_exact_positon(self, value):
#         self.arr.append(value)
#         self.size += 1
#         index = self.size - 1
#         while index > 0:
#             parent_index  = (index - 1) // 2
#             if self.arr[parent_index] < self.arr[index]:
#                 self.arr[parent_index] , self.arr[index] = self.arr[index], self.arr[parent_index]
#                 index  = parent_index
#             else :
#                 return
#     def delete(self):
#         # steps
#         # return first element of arr
#         # put last element in place of first elemnt 
#         # reduce size by 1
#         # call heapify_down with index 0
#         if self.size == 0:
#             print('Heap is empty')
#             return
#         root = self.arr[0]
#         last_element = self.arr.pop()
#         self.size -= 1

#         if self.size > 0:
#             self.arr[0] = last_element
#             self.heapify_down(0)
#         return root
#     def heapify_down(self, index):
#         largest = index
#         left_child_idx = 2 * index + 1
#         right_child_idx = 2 * index + 2

#         if left_child_idx < self.size and self.arr[left_child_idx] > self.arr[largest]:
#             largest = left_child_idx
        
#         if right_child_idx < self.size and self.arr[right_child_idx] > self.arr[largest]:
#             largest  = right_child_idx
        
#         if largest != index :
#             self.arr[index] , self.arr[largest] = self.arr[largest], self.arr[index]
#             self.heapify_down(largest)
        
#     def convert_arr_to_heap(self, lst):
#         self.size = len(lst)
#         self.arr = lst[:]
#         for i in range(self.size//2 - 1, -1, -1):
#             self.heapify_down(i)
    
#     def heap_sort(self, arr_to_sort):
#         self.convert_arr_to_heap(arr_to_sort)
#         for i in range(self.size - 1, 0, -1):
#             self.arr[0], self.arr[i]  = self.arr[i], self.arr[0]
#             self.size -= 1
#             self.heapify_down(0)
        
#         return self.arr


# heap = Heap()
# heap.insert(10)
# heap.insert(30)
# heap.insert(20)
# print(heap.arr)
# heap.insert(40)
# print(heap.arr)
# heap.insert_at_exact_positon(50)
# heap.insert_at_exact_positon(12)
# print(heap.arr)
# root  = heap.delete()
# print('Element deleted from heap is :', root)
# print(heap.arr)
# root  = heap.delete()
# print('Element deleted from heap is :', root)
# print(heap.arr)

#Convert arr to heap using heapify funciton

# lst = [1, 3, 7, 4, 10, 8, 9]
# heap.convert_arr_to_heap(lst)
# print(heap.arr)

# arr_to_sort = [4, 6, 1, 0, 9, 34, 23, 7]
# sorted_array = heap.heap_sort(arr_to_sort)
# print('Array after heap sort is :')
# print(sorted_array)

# class PriorityQueue(Heap):
#     def __init__(self):
#         super().__init__()
    
#     def insert(self, value):
#         # add new element in heap
#         super().insert(value)
#     def extract_max(self):
#         return super().delete()
#     def peek_max(self):
#         if self.size == 0:
#             print('Priority Queue is empty')
#             return None
#         return self.arr[0]
#     def increase_key(self, index, new_value):
#         # Increase the priority of a given element and maintain the heap property
#         if index >= self.size or new_value <= self.arr[index]:
#             print('Invalid Index or new Value')
#             return
#         self.arr[index] = new_value
#         self.heapify_up(index)
    
#     def decrease_key(self, index, new_value):
#          # Decrease the priority of a given element and maintain the heap property
#         if index >= self.size or new_value >= self.arr[index]:
#             print('Invalid index or new value')
#             return
        
#         self.arr[index] = new_value
#         self.heapify_down(index)

# pq = PriorityQueue()
# pq.insert(10)
# pq.insert(30)
# pq.insert(20)
# print(pq.arr)

# print('Max:', pq.peek_max())

# pq.increase_key(1, 40)  # Increase priority of element at index 1
# print('After increase:', pq.arr)

# pq.decrease_key(0, 10)  # Increase priority of element at index 0
# print('After decrease:', pq.arr)

# print('Extracted max:', pq.extract_max())
# print('After extraction:', pq.arr)


## heapq module for using it as Priority queue
# import heapq
# lst = [5, 7, 8, 1, 3]
# heapq.heapify(lst)
# print("The created heap is : ", end="")
# print(lst)

# heapq.heappush(lst, 4)
# print("The modified heap after push is : ", end="")
# print(lst)

# print("The popped and smallest element is : ", end="")
# print(heapq.heappop(lst))
# print('After pop of first element from heap:', end = "")
# print(lst)

# #heappushpop() and heapreplace() both works same as both does push and pop in one go
# print("The popped item using heappushpop() is : ", end="")
# print(heapq.heappushpop(lst, 6))

# print('After pop and push in one go from heap:', end = "")
# print(lst)

# print("The popped item using heapreplace() is : ", end="")
# print(heapq.heapreplace(lst, 10))

# print('After pop and push in one go from heap:', end = "")
# print(lst)

# print("The 3 largest numbers in list are : ", end="")
# print(heapq.nlargest(3, lst))

# print("The 3 smallest numbers in list are : ", end="")
# print(heapq.nsmallest(3, lst))



# Sliding Window Problems 


# # Maximum Subarray Sum Of Size K
# arr = [2, 4, 15, 1, 10, 2, 6]
# k = 3
# def solveBruteForce(arr, k):
#     maxi = float('-inf')
#     for i in range(len(arr)):
#         sum = 0
#         for j in range(i, i + k, 1):
#             if j < len(arr):
#                 sum += arr[j]
#         # print(sum)
#         maxi = max(maxi, sum)
#     return maxi

# def solveOptimised(arr, k):
#     maxi = float('-inf')
#     i = 0
#     sum = 0
#     for j in range(len(arr)):
#         sum += arr[j]
#         if j - i + 1 == k:
#             maxi = max(maxi, sum)
#             sum = sum - arr[i]
#             i += 1
#     return maxi


# def maximum_subarray_sum_of_size_k(arr, k):
#     # ans = solveBruteForce(arr, k)
#     ans = solveOptimised(arr, k)
#     return ans
# print(maximum_subarray_sum_of_size_k(arr, k))

# # First Negative number in every window size k
# arr = [-8, -2, 3, -6, 10, -2, 5]
# k = 3
# def solveBruteForce(arr, k):
#     ans = []
#     for i in range(len(arr) - k + 1):
#         bool  = False
#         for j in range(i, i + k, 1):
#             if arr[j] < 0:
#                 bool = True
#                 ans.append(arr[j])
#                 break
#         if not bool:
#             ans.append(0)
#     return ans
# def solveOptimised(arr, k):
#     ans = []
#     temp = []
#     i = 0
#     for j in range(len(arr)):
#         if arr[j] < 0:
#             temp.append(arr[j])
#         if j - i + 1 == k:
#             if len(temp) == 0:
#                 ans.append(0)
#             else:
#                 ans.append(temp[0])
#                 if arr[i] == temp[0]:
#                     temp.pop(0)
#             i += 1
#     return ans
            
# def first_negative_number(arr, k):
#     # ans = solveBruteForce(arr, k)\
#     ans = solveOptimised(arr, k)
#     return ans
# print(first_negative_number(arr, k))

## count occurence of anagrams 

# str = 'acbaabaa'
# pattern = 'aaba'

# def solvebySlidingWindow(str, pattern):
#     map = {}
#     for char in pattern:
#         if char in map.keys():
#             map[char] += 1
#         else :
#             map[char]  = 1
#     i = 0
#     count = len(map)
#     k = len(pattern)
#     ans = 0
#     # print(count)
#     for j in range(len(str)):
#         if str[j] in map:
#             map[str[j]] -= 1
#             if map[str[j]] == 0:
#                 count -= 1
#         if j - i + 1 == k:
#             if count == 0:
#                 ans += 1
        
#             if str[i] in map:
#                 if map[str[i]] == 0:
#                     count += 1
#                 map[str[i]] +=1
#             i += 1
#     return ans
# def count_occurence_of_anagrams(str, pattern):
#     ans = solvebySlidingWindow(str, pattern)
#     return ans
# print(count_occurence_of_anagrams(str, pattern))


# # maximum of all subarray of size k
# arr = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3
# def solvemorethanBruteForce(arr, k):
#     ans = []
#     temp = []
#     i = 0
#     for j in range(len(arr)):
#         temp.append(arr[j])
#         if j - i + 1 == k:
#             maxi = max(temp)
#             ans.append(maxi)
#             if arr[i] == maxi:
#                 temp.remove(maxi)
#             i += 1
#     return ans
# from collections import deque
# def solveSpaceOptimised(arr, k):
#     queue = deque()
#     i = 0
#     ans = []
#     for j in range(len(arr)):
        
#         while queue and queue[-1] < arr[j]:
#             queue.pop()

#         queue.append(arr[j])
#         if j - i + 1 == k:
#             ans.append(queue[0])
#             if arr[i] == queue[0]:
#                 queue.popleft()
#             i += 1
#     return ans

# def maxOfAllSubarrayOfSizeK(arr, k):
#     # ans = solvemorethanBruteForce(arr, k)
#     ans  = solveSpaceOptimised(arr, k)
#     return ans
# print(maxOfAllSubarrayOfSizeK(arr, k))


# # minimum of all subarray of size k
# arr = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3
# from collections import deque
# def solveSpaceOptimised(arr, k):
#     i = 0
#     queue = deque()
#     ans = []
#     for j in range(len(arr)):

#         while queue and queue[-1] > arr[j]:
#             queue.pop()
#         queue.append(arr[j])

#         if j - i + 1 == k:
#             ans.append(queue[0])
#             if arr[i] == queue[0]:
#                 queue.popleft()
#             i += 1
#     return ans

# def minOfAllSubarrayOfSizeK(arr, k):
#     ans  = solveSpaceOptimised(arr, k)
#     return ans
# print(minOfAllSubarrayOfSizeK(arr, k))


# largest Subarray of Sum K with all value positive

# arr = [10, 5, 2, 7, 1, 9]
# k = 15
# def solveSlidingWindow(arr, k):
#     maxi = float('-inf')
#     i = 0
#     sum = 0
#     for j in range(len(arr)):
#         sum += arr[j]
#         while sum > k and i <= j:
#             sum  -= arr[i]
#             i += 1
#         if sum == k:
#             maxi = max(maxi, j - i + 1)
#     return maxi if maxi != float('-inf') else 0


# def largest_subarray_of_sum_K(arr, k):
#     ans = solveSlidingWindow(arr, k)
#     return ans
# print(largest_subarray_of_sum_K(arr, k))



# largest Subarray of Sum K with all values positive and negative 

# arr = [-1, 3, 10, 5, 2, 7, 1, -6, 9]
# k = 10
# def solveSlidingWindow(arr, k):
#     maxi = 0
#     prefix_sum_map = {0 : -1} # really essential if subarray start from 0th index 
#     prefix_sum = 0
#     for j in range(len(arr)):
#         prefix_sum += arr[j]
#         if prefix_sum - k in prefix_sum_map:
#             maxi = max(maxi, j - prefix_sum_map[prefix_sum - k])
#         if prefix_sum not in prefix_sum_map:
#             prefix_sum_map[prefix_sum] = j
#     return maxi

# def largest_subarray_of_sum_K(arr, k):
#     ans = solveSlidingWindow(arr, k)
#     return ans
# print(largest_subarray_of_sum_K(arr, k))


# # Find the longest substring with k unique characters in a given string
# str = 'aabbbbccdedeec'
# k = 2
# def solveSlidingWindow(str, k):
#     maxi = float('-inf')
#     map = {}
#     i = 0
#     for j in range(len(str)):
#         if str[j] in map:
#             map[str[j]] += 1
#         else :
#             map[str[j]] = 1
#         while len(map) > k and i <= j:
#             map[str[i]] -= 1
#             if map[str[i]] == 0:
#                 map.pop(str[i])
#             i += 1
#         if len(map) == k:
#             maxi = max(maxi, j - i + 1)
#     return maxi

# def longest_substring_with_k_unique_characters(str, k):
#     ans = solveSlidingWindow(str, k)
#     return ans
# print(longest_substring_with_k_unique_characters(str, k))


# # Find the longest substring with without repeating characters in a given string
# str = "pwwkew"

# def solveSlidingWindow(str):
#     map = {}
#     i = 0
#     maxi = -1
#     for j in range(len(str)):
#         if str[j] in map:
#             map[str[j]] += 1
#         else :
#             map[str[j]] = 1
#         while len(map) < j - i + 1 and i <= j:
#             map[str[i]] -= 1
#             if map[str[i]] == 0:
#                 map.pop(str[i])
#             i += 1
#         if len(map) == j - i + 1:
#             maxi = max(maxi, j - i + 1)
#     return maxi 

# # efficient approach 
# def solveSlidingWindow2(str):
#     map = {}
#     i = 0
#     maxi = 0
#     for j in range(len(str)):
#         if str[j] in map:
#             i = max(i, map[str[j]] + 1)
#         map[str[j]]  = j
#         maxi = max(maxi, j - i + 1)
#     return maxi
            

# def longest_substring_without_repeating_characters(str):
#     # ans = solveSlidingWindow(str)
#     ans = solveSlidingWindow2(str)
#     return ans
# print(longest_substring_without_repeating_characters(str))



# # leetcode 904. Fruit Into Baskets

# fruits = [0,1,2,2]
# def solveSlidingWindow(arr):
#     i = 0
#     maxi = 0
#     k = 2 # atmost two types of fruits to pick
#     map = {}
#     for j in range(len(arr)):
#         if arr[j] in map:
#             map[arr[j]] += 1
#         else :
#             map[arr[j]]  = 1

#         while len(map) > k and i <= j:
#             map[arr[i]] -= 1
#             if map[arr[i]] == 0:
#                 map.pop(arr[i])
#             i += 1
#         maxi = max(maxi, j - i + 1)
#     return maxi 

# def total_fruit(fruits):
#     ans = solveSlidingWindow(fruits)
#     return ans
# print(total_fruit(fruits))

# # Minimum Window Sustring
# str = 'this is a test string'
# pattern = 'tist'

# def solveSlidingWindow(str, pattern):
#     if not str or not pattern:
#         return ""
#     map = {}
#     for char in pattern:
#         if char in map:
#             map[char] += 1
#         else:
#             map[char] = 1
#     i = 0
#     mini = float('inf')
#     count  = len(map)
#     min_start = 0
#     for j in range(len(str)):
#         if str[j] in map:
#             map[str[j]] -= 1
#             if map[str[j]] == 0:
#                 count -= 1 
#         while count == 0:
#             if j - i + 1 < mini:
#                 mini = j - i + 1
#                 min_start = i
#             if str[i] in map:
#                 map[str[i]] += 1
#                 if map[str[i]] > 0:
#                     count += 1
#             i += 1
#     if mini == float('inf'):
#         return ""
#     else:
#         return str[min_start:min_start + mini]
#         # return mini
         

# def minimum_window_substring(str, pattern):
#     ans = solveSlidingWindow(str, pattern)
#     return ans
# print(minimum_window_substring(str, pattern))



# # KADANE'S algorithm for Largest Sum Contiguous array
# arr = [-2,-3,4,-1,-2,1,5,-3]
# def largest_sum_in_contiguous_array(arr):
#     curr_sum = 0
#     max_sum = arr[0]
#     for i in range(len(arr)):
#         curr_sum += arr[i]
#         max_sum = max(max_sum, curr_sum)
#         if curr_sum < 0:
#             curr_sum = 0
#     return max_sum

# print(largest_sum_in_contiguous_array(arr))

# # updated KADANE'S algorithm for returning Largest Sum Contiguous array 
# def largest_sum_in_contiguous_array(arr):
#     curr_sum = 0
#     max_sum = arr[0]
#     start = end = temp_start = 0
    
#     for i in range(len(arr)):
#         curr_sum += arr[i]
        
#         if curr_sum > max_sum:
#             max_sum = curr_sum
#             start = temp_start
#             end = i
        
#         if curr_sum < 0:
#             curr_sum = 0
#             temp_start = i + 1
    
#     max_subarray = arr[start:end + 1]
#     return max_sum, max_subarray

# # Example usage:
# arr = [-2, -3, 4, -1, -2, 1, 5, -3]
# max_sum, max_subarray = largest_sum_in_contiguous_array(arr)
# print(f"The maximum sum is {max_sum} and the subarray is {max_subarray}")

# arr2 = [-2, -3, -1, -5]
# max_sum, max_subarray = largest_sum_in_contiguous_array(arr2)
# print(f"The maximum sum is {max_sum} and the subarray is {max_subarray}")


# ## Binary Search Tree
# from collections import deque
# class Node:
#     def __init__(self, data: int):
#         self.data = data
#         self.left = None
#         self.right = None

#     def insert(self, data: int):
#         if data < self.data:
#             if self.left is None:
#                 self.left = Node(data)
#             else:
#                 self.left.insert(data)
#         elif data > self.data:
#             if self.right is None:
#                 self.right = Node(data)
#             else:
#                 self.right.insert(data)
#         # Do nothing if data == self.data (ignoring duplicates)

#     def delete(self, data: int):
#         if data < self.data:
#             if self.left:
#                 self.left = self.left.delete(data)
#         elif data > self.data:
#             if self.right:
#                 self.right = self.right.delete(data)
#         else:
#             # Node to be deleted found
#             if self.left is None and self.right is None:
#                 # Case 1: Node is a leaf
#                 return None
#             elif self.left is None:
#                 # Case 2: Node has one child (right)
#                 return self.right
#             elif self.right is None:
#                 # Case 2: Node has one child (left)
#                 return self.left
#             else:
#                 # Case 3: Node has two children then we will found inorder successor
#                 min_larger_node = self.right.get_min()
#                 self.data = min_larger_node.data
#                 self.right = self.right.delete(min_larger_node.data)
        
#         return self

#     def get_min(self):
#         current = self
#         while current.left is not None:
#             current = current.left
#         return current

#     def print_tree(self):
#         """Prints the tree in-order (left-root-right)."""
#         if self.left:
#             self.left.print_tree()
#         print(self.data, end=' ')
#         if self.right:
#             self.right.print_tree()

#     def inorder_traversal(self):
#         """In-order traversal (left-root-right)."""
#         if self.left:
#             self.left.inorder_traversal()
#         print(self.data, end=' ')
#         if self.right:
#             self.right.inorder_traversal()

#     def pre_order_traversal(self):
#         """Pre-order traversal (root-left-right)."""
#         print(self.data, end=' ')
#         if self.left:
#             self.left.pre_order_traversal()
#         if self.right:
#             self.right.pre_order_traversal()

#     def post_order_traversal(self):
#         """Post-order traversal (left-right-root)."""
#         if self.left:
#             self.left.post_order_traversal()
#         if self.right:
#             self.right.post_order_traversal()
#         print(self.data, end=' ')
    
#     def level_order_traversal(self):
#         if not self:
#             return None
#         queue = deque([self])

#         while queue:
#             node = queue.popleft()
#             print(node.data, end = ' ')

#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
        
#     def search(self, data: int) -> bool:
#         if data < self.data:
#             return self.left.search(data) if self.left else False
#         elif data > self.data:
#             return self.right.search(data) if self.right else False
#         return True

#     def height(self) -> int:
#         left_height = self.left.height() if self.left else -1
#         right_height = self.right.height() if self.right else -1
#         return max(left_height, right_height) + 1

#     def is_balanced(self) -> bool:
#         if not self:
#             return True
        
#         # Get the heights of the left and right subtrees
#         left_height = self.left.height() if self.left else -1
#         right_height = self.right.height() if self.right else -1
        
#         # Check if the height difference is within the allowed range
#         height_diff = abs(left_height - right_height)
#         if height_diff > 1:
#             return False
        
#         # Recursively check if the left and right subtrees are balanced
#         left_balanced = self.left.is_balanced() if self.left else True
#         right_balanced = self.right.is_balanced() if self.right else True
        
#         return left_balanced and right_balanced

# # Example usage
# root = Node(15)
# root.insert(10)
# root.insert(20)
# root.insert(8)
# root.insert(12)
# root.insert(17)
# root.insert(25)

# print("pre-order traversal:")
# root.pre_order_traversal()
# print()

# print("post-order traversal:")
# root.post_order_traversal()
# print()

# print("in-order traversal:")
# root.inorder_traversal()
# print()

# print("Level-order traversal:")
# root.level_order_traversal()
# print()

# print("In-order traversal before deletion:")
# root.inorder_traversal()
# print()

# root.delete(8)
# print("In-order traversal after deleting 8 (leaf node):")
# root.inorder_traversal()
# print()

# root.delete(10)
# print("In-order traversal after deleting 10 (node with one child):")
# root.inorder_traversal()
# print()

# root.delete(15)
# print("In-order traversal after deleting 15 (node with two children):")
# root.inorder_traversal()
# print()


# print(root.search(15))
# print(root.height())
# print(root.is_balanced())

# # build tree from preorder and inorder traversal of tree
# preorder = [3, 9, 20, 15, 7]
# inorder = [9, 3, 15, 20, 7]

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
# def build_tree(preorder, inorder):
#     if not preorder or not inorder:
#         return None
#     # The first element of preorder list is the root
#     root_value = preorder.pop(0)
#     root  = Node(root_value)

#     # Find the index of the root in inorder list
#     inorder_index  = inorder.index(root_value)

#     # Elements to the left of the root in inorder list form the left subtree
#     left_inorder = inorder[: inorder_index]

#     # Elements to the right of the root in inorder list form the right subtree
#     right_inorder = inorder[inorder_index + 1:]

#     # Recursively build the left and right subtrees
#     root.left = build_tree(preorder, left_inorder)
#     root.right = build_tree(preorder, right_inorder)

#     return root

# def print_post(root):
#     if root:
#         print_post(root.left)
#         print_post(root.right)
#         print(root.data, end = ' ')
    
# root = build_tree(preorder, inorder)

# print("Post order traversal of the constructed tree:")
# print_post(root)
# print()


# # build tree from postOrder and inorder traversal of tree
# postorder = [9, 15, 7, 20, 3]
# inorder = [9, 3, 15, 20, 7]

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
# def build_tree(postorder, inorder):
#     if not postorder or not inorder:
#         return None
#     root_value = postorder.pop()
#     root = Node(root_value)
#     inorder_index  = inorder.index(root_value)

#     inorder_left = inorder[:inorder_index]

#     inorder_right = inorder[inorder_index + 1 :]


#     root.right = build_tree(postorder, inorder_right)

#     root.left = build_tree(postorder, inorder_left)
    
#     return root

# def print_pre_order(root):
#     if root:
#         print(root.data, end = ' ')
#         print_pre_order(root.left)
#         print_pre_order(root.right)

# root = build_tree(postorder, inorder)
# print_pre_order(root)
# print()


## Garphs 
# we can implement graph by two ways 1. Adjacency List 2.Adjacency Matrix

# # basic implementation of an undirected, unweighted graph using an adjacency list:

# class Graph:
#     def __init__(self):
#         self.adjacency_list = {}
#     def add_vertex(self, vertex):
#         if vertex not in self.adjacency_list:
#             self.adjacency_list[vertex] = []

#     def add_edge(self, vertex1, vertex2):
#         if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
#             self.adjacency_list[vertex1].append(vertex2)
#             self.adjacency_list[vertex2].append(vertex1)

#     def remove_edge(self, vertex1, vertex2):
#         if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
#             if vertex2 in self.adjacency_list[vertex1]:
#                 self.adjacency_list[vertex1].remove(vertex2)
#             if vertex1 in self.adjacency_list[vertex2]:
#                 self.adjacency_list[vertex2].remove(vertex1)
    
#     def remove_vertex(self, vertex):
#         if vertex in self.adjacency_list:
#             for other_vertex in list(self.adjacency_list[vertex]):
#                 self.remove_edge(vertex, other_vertex)
#             del self.adjacency_list[vertex]

#     def has_edge(self, vertex1, vertex2):
#         return vertex1 in self.adjacency_list and vertex2 in self.adjacency_list[vertex1]
    
#     def get_neighbors(self, vertex):
#         return self.adjacency_list[vertex] if vertex in self.adjacency_list else []
    
#     def print_graph(self):
#         for vertex in self.adjacency_list:
#             print(f"{vertex}: {self.adjacency_list[vertex]}")
# graph  = Graph()
# graph.add_vertex('A')
# graph.add_vertex('B')
# graph.add_vertex('C')
# graph.add_edge('A', 'B')
# graph.add_edge('A', 'C')
# graph.print_graph()
# print("\nRemoving edge A-C")
# graph.remove_edge('A', 'C')
# graph.print_graph()
# print("\nRemoving vertex A")
# graph.remove_vertex('A')
# graph.print_graph()
# print("\nHas edge B-C:", graph.has_edge('B', 'C'))
# print("Neighbors of B:", graph.get_neighbors('B'))



# #basic implementation of a directed, weighted graph using an adjacency list:

# class WeightedGraph:
#     def __init__(self):
#         self.adjacency_list = {}
#     def add_vertex(self, vertex):
#         if vertex not in self.adjacency_list:
#             self.adjacency_list[vertex] = []
#     def add_weighted_edge(self, vertex1, vertex2, weight):
#         if  vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
#             self.adjacency_list[vertex1].append((vertex2, weight))
#     def print_graph(self):
#         for vertex in self.adjacency_list:
#             print(f"{vertex}: {self.adjacency_list[vertex]}")

# graph = WeightedGraph()
# graph.add_vertex('A')
# graph.add_vertex('B')
# graph.add_vertex('C')
# graph.add_weighted_edge('A', 'B', 1)
# graph.add_weighted_edge('A', 'C', 2)
# graph.add_weighted_edge('B', 'C', 3)
# graph.print_graph()


# # basic implementation of an undirected, unweighted graph using an adjacency matrix:

# class GraphMatrix:
#     def __init__(self, num_vertices):
#         self.num_vertices = num_vertices
#         self.adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]
#     def add_edge(self, vertex1, vertex2):
#         if 0 <= vertex1 < self.num_vertices and 0 <= vertex2 < self.num_vertices:
#             self.adjacency_matrix[vertex1][vertex2] = 1
#             self.adjacency_matrix[vertex2][vertex1] = 1
#     def remove_edge(self, vertex1, vertex2):
#         if 0 <= vertex1 < self.num_vertices and 0 <= vertex2 < self.num_vertices:
#             self.adjacency_matrix[vertex1][vertex2] = 0
#             self.adjacency_matrix[vertex2][vertex1] = 0
#     def remove_vertex(self, vertex):
#         if 0 <= vertex < self.num_vertices:
#             for i in range(self.num_vertices):
#                 self.adjacency_matrix[vertex][i] = 0
#                 self.adjacency_matrix[i][vertex] = 0
    
#     def has_edge(self, vertex1, vertex2):
#         return self.adjacency_matrix[vertex1][vertex2] != 0
    
#     def get_neighbors(self, vertex):
#         # return [i for i, is_edge in enumerate(self.adjacency_matrix[vertex]) if is_edge]
#         neighbors = []
#         if 0 <= vertex < self.num_vertices:
#             for i in range(self.num_vertices):
#                 if self.adjacency_matrix[vertex][i] != 0:
#                     neighbors.append(i)
#         return neighbors
#     def print_graph(self):
#         for row in self.adjacency_matrix:
#             print(row)
    
# graph = GraphMatrix(4)
# graph.add_edge(0, 1)
# graph.add_edge(0, 2)
# graph.add_edge(1, 2)
# graph.add_edge(2, 3)
# graph.print_graph()
# print("\nRemoving edge 0-2")
# graph.remove_edge(0, 2)
# graph.print_graph()
# print("\nRemoving vertex 1")
# graph.remove_vertex(1)
# graph.print_graph()
# print("\nHas edge 2-3:", graph.has_edge(2, 3))
# print("Neighbors of 2:", graph.get_neighbors(2))


# basic implementation of a directed, weighted graph using an adjacency matrix:

# class WeightedGraphMatrix:
#     def __init__(self, num_vertices):
#         self.num_vertices = num_vertices
#         self.adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]
#     def add_edge(self, vertex1, vertex2, weight):
#         if 0 <= vertex1 < self.num_vertices and 0 <= vertex2 < self.num_vertices:
#             self.adjacency_matrix[vertex1][vertex2] = weight
#     def remove_edge(self, vertex1, vertex2):
#         if 0 <= vertex1 < self.num_vertices and 0 <= vertex2 < self.num_vertices:
#             self.adjacency_matrix[vertex1][vertex2] = 0

#     def print_graph(self):
#         for row in self.adjacency_matrix:
#             print(row)
    
# graph = WeightedGraphMatrix(4)
# graph.add_edge(0, 1, 2)
# graph.add_edge(0, 2, 4)
# graph.add_edge(1, 2, 1)
# graph.add_edge(2, 3, 3)
# graph.print_graph()

# from collections import deque
# adjacency_list = {}
# adjacency_list[0] = [1]
# adjacency_list[1] = [0, 2, 3]
# adjacency_list[2] = [1, 4]
# adjacency_list[3] = [1, 4]
# adjacency_list[4] = [2, 3]

# # adjacency_list[5] = []

# def bfs(start_vertex, visited, adjacency_list):
#     queue = deque()
#     queue.append(start_vertex)
#     visited.add(start_vertex)
#     while queue:
#         vertex = queue.popleft()
#         print(vertex, end = ' ')
#         for neighbour in adjacency_list[vertex]:
#             if neighbour not in visited:
#                 queue.append(neighbour)
#                 visited.add(neighbour)  
# def dfs(start_vertex, visited, adjacency_list):
#     visited.add(start_vertex)
#     print(start_vertex, end=' ')

#     for neighbour in adjacency_list[start_vertex]:
#         if neighbour not in visited:
#             dfs(neighbour, visited, adjacency_list)
                
# def graphTraversal(adjacency_list):
#     visited = set()
#     for vertex in adjacency_list:
#         if vertex not in visited:
#             # bfs(vertex, visited, adjacency_list)
#             dfs(vertex, visited, adjacency_list)
#     print()
    
# graphTraversal(adjacency_list)

# def modified_dfs(source, adjacency_list, target, visited, path):
#     if source == target:
#         print(path)
#         return
#     visited.add(source)
#     for neighbour in adjacency_list[source]:
#         if neighbour not in visited:
#             modified_dfs(neighbour, adjacency_list, target, visited, path + [neighbour])
#     visited.remove(source)
# def print_all_possible_paths(adjacency_list, source, target):
#     visited = set()
#     path = [source]
#     modified_dfs(source, adjacency_list, target, visited, path)
# print_all_possible_paths(adjacency_list, 0, 4)


# #Detect cycle in undirected graph
# adjacency_list = {}
# adjacency_list[0] = [1]
# adjacency_list[1] = [0, 2, 3]
# adjacency_list[2] = [1, 3]
# adjacency_list[3] = [1, 2]

# def modified_dfs(start_vertex, adjacency_list, visited, parent):
#     visited.add(start_vertex)
    
#     for neighbour in adjacency_list[start_vertex]:
#         if neighbour not in visited:
#             if modified_dfs(neighbour, adjacency_list, visited, start_vertex):
#                return True
#         elif neighbour != parent:
#             return True
#     return False

# def hasCycle(adjacency_list):
#     visited = set()
#     parent = -1
#     for vertex in adjacency_list:
#         if vertex not in visited:
#            if modified_dfs(vertex, adjacency_list, visited, parent):
#             return True
#     return False
# print(hasCycle(adjacency_list))

# # Detect cycle in directed graph
# adjacency_list = {}
# adjacency_list[0] = [1]
# adjacency_list[1] = [3]
# adjacency_list[2] = [1]
# adjacency_list[3] = [2]

# def modified_dfs(start_vertex, adjacency_list, visited, recursion_arr):
#     visited.add(start_vertex)
#     recursion_arr[start_vertex] = True
    
#     for neighbour in adjacency_list[start_vertex]:
#         if neighbour not in visited:
#             if modified_dfs(neighbour, adjacency_list, visited, recursion_arr):
#                 return True
#         elif recursion_arr[neighbour] == True:
#             return True
        
#     recursion_arr[start_vertex] = False
#     return False
# def has_cycle(adjacency_list):
#     visited = set()
#     recursion_arr = [False] * len(adjacency_list) 
#     for vertex in adjacency_list:
#         if vertex not in visited:
#             if modified_dfs(vertex, adjacency_list, visited, recursion_arr):
#                 return True
#     return False
# print(has_cycle(adjacency_list))
        

# # topological sorting for DAG(directed acyclic graph)
# adjacency_list = {}
# adjacency_list[0] = [1]
# adjacency_list[1] = [0, 4]
# adjacency_list[2] = [3]
# adjacency_list[3] = [2, 4]
# adjacency_list[4] = [1, 3]
# def modified_dfs(start_vertex, adjacency_list, visited, stack):
#     visited[start_vertex] = True
#     for neighbour in adjacency_list.get(start_vertex, []):
#         if not visited[neighbour]:
#             modified_dfs(neighbour, adjacency_list, visited, stack)
#     stack.append(start_vertex)
# def top_sort(adjacency_list):
#     stack = []
#     visited = [False] * len(adjacency_list)
#     for vertex in adjacency_list:
#         if not visited[vertex]:
#             modified_dfs(vertex, adjacency_list, visited, stack)
#     return stack
# ansStack = top_sort(adjacency_list)

# while ansStack:
#     print(ansStack.pop())


# #Djikstra Algorithm - to find the shortest path from source to all nodes for weighted graph and weight should always be positive
# import heapq
# adjacency_list = {}
# adjacency_list[0] = [(1, 2), (2, 4)]
# adjacency_list[1] = [(2, 1), (3, 3)]
# adjacency_list[2] = [(4, 6)]
# adjacency_list[3] = [(4, 2)]
# adjacency_list[4] = [(5, 1)]
# adjacency_list[5] = [(3, 4)]
# V = 5

# def modified_bfs_for_djikstra(visited, dist, source):
#     priorityqueue = []
#     heapq.heappush(priorityqueue, (0, source))
#     while priorityqueue:
#         current_dist, vertex = heapq.heappop(priorityqueue)
#         visited[vertex] = True
#         for neighbour, weight in adjacency_list[vertex]:
#             if not visited[neighbour]:
#                 # perform relaxation 
#                 if current_dist + weight < dist[neighbour]:
#                     dist[neighbour] = current_dist + weight
#                     heapq.heappush(priorityqueue, (dist[neighbour], neighbour))

# def djikstra_algo(adjacency_list, source):
#     visited = [False] * len(adjacency_list)
#     dist = [float('inf')] * len(adjacency_list)
#     dist[source] = 0
#     modified_bfs_for_djikstra(visited, dist, source)
#     return dist

# ans = djikstra_algo(adjacency_list, 0)
# print(ans)


# #Bellmen ford algorithm - this algorithm find me shortest path from source node to all nodes whether it conatins negative weight . but it should not contain negative weight cycle(sum of total weight of cycle formed should not be negative)
# adjacency_list = {}
# adjacency_list[0] = [(1, 2), (2, 4)]
# adjacency_list[1] = [(2, 1), (3, 3)]
# adjacency_list[2] = [(4, -6)]
# adjacency_list[3] = [(4, -2)]
# adjacency_list[4] = [(5, 1)]
# adjacency_list[5] = [(3, 4)]
# source = 0
# def bellmen_ford_algo(adjacency_list, source):
#     dist = [float('inf')] * len(adjacency_list)
#     dist[source] = 0
#     for _ in range(len(adjacency_list) - 1):
#         for vertex  in adjacency_list:
#             for neighbour, weight in adjacency_list[vertex]:
                    # perform relaxation
#                 if dist[vertex] != float('inf') and dist[vertex] + weight < dist[neighbour]:
#                     dist[neighbour] = dist[vertex] + weight

#     # check negative cycle exist in graph
#     for vertex in adjacency_list:
#         for neighbour, weight in adjacency_list[vertex]:
#             if dist[vertex] != float('inf') and dist[vertex] + weight < dist[neighbour]:
#                 print('Negative Cycle Exists in this graph.')
    
#     return dist
    
# distances = bellmen_ford_algo(adjacency_list, source)

# if distances is not None:
#     print(distances)

# # Prims Algorithm -> this algorithm is used to find MST(minimum spanning tree -> minimum number of edges required to connect all vertex with minimum total weight)
# # for this algo we use two sets - one is visited array and second is priority queue and use BFS
# adjacency_list = {}
# adjacency_list[0] = [(1, 5), (2, 7), (3, 10)]
# adjacency_list[1] = [(0, 5), (3, 11)]
# adjacency_list[2] = [(0, 7), (3, 12)]
# adjacency_list[3] = [(0, 10), (2, 12), (1, 11)]
# import heapq
# def modified_bfs(adjacency_list, visited, startvertex):
#     mstcost = 0
#     mst_edges = []
#     priorityqueue = []
#     heapq.heappush(priorityqueue, (0, startvertex, -1)) #( weight, vertex, parent )

#     while priorityqueue:
#         min_weight, vertex, parent = heapq.heappop(priorityqueue)
#         if not visited[vertex]:
#             mstcost += min_weight
#             visited[vertex] = True
#             if parent != -1:  # Avoid adding the first "fake" edge
#                 mst_edges.append((parent, vertex, min_weight))
#             for neighbour, weight in adjacency_list[vertex]:
#                 if not visited[neighbour]:
#                     heapq.heappush(priorityqueue, (weight, neighbour, vertex))
#     return mstcost, mst_edges            

# def prims_algo(adjacency_list):
#     visited = [False] * len(adjacency_list)
#     mst_edges = []
#     total_mst_cost = 0

#     for vertex in adjacency_list:
#         if not visited[vertex]:
#             mstcost, edges = modified_bfs(adjacency_list, visited, vertex)
#             total_mst_cost += mstcost
#             mst_edges.extend(edges)

#     return total_mst_cost, mst_edges

# mst_cost, mst_edges = prims_algo(adjacency_list)
# print('Cost for MST is:', mst_cost)
# print('Edges in the MST are:', mst_edges)

# # SCC(Strongly Connected Components in graphs) using kosaraju's algo
# #conditions -> graph shoud be directed
# # step 1 -> add all the vertex in new graph using toplogical sort
# # step 2 -> transpose the graph
# # step 3 -> call DFS for all vertex from transposed graph

# adjacency_list = {}
# adjacency_list[0] = [2, 4]
# adjacency_list[1] = [3]
# adjacency_list[2] = [1]
# adjacency_list[3] = [2]
# adjacency_list[4] = [5]
# adjacency_list[5] = [6]
# adjacency_list[6] = [4]
# def dfs_top_sort(adjacency_list, start_vertex, visited, stack_top_sort):
#     visited[start_vertex] = True

#     for neighbour in adjacency_list[start_vertex]:
#         if not visited[neighbour]:
#             dfs_top_sort(adjacency_list, neighbour, visited, stack_top_sort)
    
#     stack_top_sort.append(start_vertex)

# def dfs(adjacencylist, visited, start_vertex):
#     visited[start_vertex] = True
#     print(start_vertex, end = ' ')

#     for neighbour in adjacencylist[start_vertex]:
#         if not visited[neighbour]:
#             dfs(adjacencylist, visited, neighbour)

# def kosaraju_algo(adjacency_list):
#     #step1 -> push all the vertex in stack using top_sort
#     stack_top_sort = []
#     visited = [False] * len(adjacency_list)

#     for vertex in adjacency_list:
#         if not visited[vertex]:
#             dfs_top_sort(adjacency_list, vertex, visited, stack_top_sort)
    
#     #step2 -> transpose the graph
#     transpose_graph = {}
#     for vertex in adjacency_list:
#         visited[vertex] = False
#         transpose_graph[vertex] = []
    
#     for vertex in adjacency_list:
#         for neighbour in adjacency_list[vertex]:
#             transpose_graph[neighbour].append(vertex)

#     #step3 -> call dfs for all vertex from transposed graph
#     print("Strongly Connected Components:")
#     while stack_top_sort:
#         vertex = stack_top_sort.pop()
#         if not visited[vertex]:
#             dfs(transpose_graph, visited, vertex)
#             print() 

# kosaraju_algo(adjacency_list)
    


# # bridge in graph using Tarjan's Algo -> bridge means if we remove any edge from graph then that graph becomes disconnected
# # we will use two array one for discovery time and other for lowest_discovery_time

# adjacency_list = {}

# adjacency_list[0] = [1, 2, 3]
# adjacency_list[1] = [0, 2]
# adjacency_list[2] = [0, 1]
# adjacency_list[3] = [0, 4]
# adjacency_list[4] = [3]

# def modified_dfs(start_vertex, graph, visited, dt, lt, time, parent):
#     visited[start_vertex] = True
#     # time[0] += 1  # Increment the global time
#     # dt[start_vertex] = time[0]
#     # lt[start_vertex] = time[0]
#     time += 1
#     dt[start_vertex] = time
#     lt[start_vertex] = time

#     for neighbour in graph[start_vertex]:
#         if neighbour == parent:
#             continue
#         elif not visited[neighbour]:
#             modified_dfs(neighbour, graph, visited, dt, lt, time, start_vertex)
#             lt[start_vertex] = min(lt[start_vertex], lt[neighbour])
#             if dt[start_vertex] < lt[neighbour]:
#                 print('Bridge is :', start_vertex, '----', neighbour)
#         elif neighbour != parent:  # means cycle exist or backedge exist
#             lt[start_vertex] = min(lt[start_vertex], dt[neighbour]) 


# def bridge_in_graph(graph):
#     visited = [False] * len(graph)
#     dt = [0] * len(graph)
#     lt = [0] * len(graph)
#     # time = [0]  # Use a list to pass by reference
#     time = 0
#     for vertex in graph:
#         if not visited[vertex]:
#             time  = modified_dfs(vertex, graph, visited, dt, lt, time, -1)

# bridge_in_graph(adjacency_list)

# # articulation point -> A vertex in an undirected connected graph is an articulation point(or cut vertex) if removing it (and edges through it) disconnects the graph
# # we will use trajan algorithm.
# adjacency_list = {}

# adjacency_list[0] = [1, 2, 3]
# adjacency_list[1] = [0, 2]
# adjacency_list[2] = [0, 1]
# adjacency_list[3] = [0, 4]
# adjacency_list[4] = [3]

# def modified_dfs(curr_vertex, visited, adjacency_list, dt, lt, articulation_arr, time, parent):
#     children = 0
#     visited[curr_vertex] = True
#     time += 1
#     dt[curr_vertex] = time
#     lt[curr_vertex] = time

#     for neighbour in adjacency_list[curr_vertex]:
#         if neighbour == parent:
#             continue
#         elif not visited[neighbour]:
#             time  = modified_dfs(neighbour, visited, adjacency_list, dt, lt, articulation_arr, time, curr_vertex)
#             lt[curr_vertex] = min(lt[curr_vertex], lt[neighbour])
#             if parent != -1 and dt[curr_vertex] <= lt[neighbour]:
#                 if curr_vertex not in articulation_arr:
#                     articulation_arr.append(curr_vertex)
#             children += 1
#         elif neighbour != parent: # backedge or cycle exist
#             lt[curr_vertex] = min(lt[curr_vertex], dt[neighbour])

#     # If the current vertex is root (parent == -1) and has more than one child, it's an articulation point
#     if parent == -1 and children > 1:
#         articulation_arr.append(curr_vertex)

# def articulation_points(adjacency_list):
#     visited = [False] * len(adjacency_list)
#     dt = [0] * len(adjacency_list)
#     lt = [0] * len(adjacency_list)
#     articulation_arr = []
#     time  = 0
#     for vertex in adjacency_list:
#         if not visited[vertex]:
#             time  = modified_dfs(vertex, visited, adjacency_list, dt, lt, articulation_arr, time, -1)

#     print("Articulation points:", articulation_arr)
# articulation_points(adjacency_list)


# # binary tree 
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


# class BinaryTree:
#     def __init__(self, data):
#         self.root = Node(data)

#     def insert(self, data):
#         node = Node(data)
#         if self.root is None:
#             self.root = node
#             return
#         queue = [self.root]
#         while queue:
#             curr_node = queue.pop(0)
#             if curr_node.left is None:
#                 curr_node.left = node
#                 break
#             else:
#                 queue.append(curr_node.left)
#             if curr_node.right  is None:
#                 curr_node.right = node
#                 break
#             else:
#                 queue.append(curr_node.right)
    
#     def inorder_traversal(self):
#         if self.root:
#             self._inorder_traversal(self.root)

#     def _inorder_traversal(self, node):
#         if node.left:
#             self._inorder_traversal(node.left)
#         print(node.value, end=' ')
#         if node.right:
#             self._inorder_traversal(node.right)
    
#     def delete_node(self, key):
#         if self.root is None:
#             return
#         if self.root.left is None or self.root.right is None:
#             if self.root.value == key:
#                 self.root = None
#             return

#         key_node = None
#         queue = [self.root]
#         while queue:
#             curr_node = queue.pop(0)

#             if curr_node.value == key:
#                 key_node = curr_node

#             if curr_node.left:
#                 queue.append(curr_node.left)
#             if curr_node.right:
#                 queue.append(curr_node.right)

#         if key_node:
#             deepest_node = curr_node 
#             key_node.value = deepest_node.value
#             self.delete_deepest_node(self.root, deepest_node)   

#     def delete_deepest_node(self, root, deepest_node):
#         queue = [root]

#         while queue:
#             curr_node = queue.pop(0)

#             if curr_node is deepest_node:
#                 curr_node = None
#                 return
            
#             if curr_node.right:
#                 if curr_node.right is deepest_node:
#                     curr_node.right = None
#                     return
#                 else:
#                     queue.append(curr_node.right)
            
#             if curr_node.left:
#                 if curr_node.left is deepest_node:
#                     curr_node.left  = None
#                     return
#                 else:
#                     queue.append(curr_node.left)

# tree = BinaryTree(1)
# tree.insert(2)
# tree.insert(3)
# tree.insert(4)
# tree.insert(5)

# print("Inorder Traversal of the Tree:")
# tree.inorder_traversal()
# print()

# print('delete node from a binary tree')
# tree.delete_node(3)

# print("\nInorder Traversal after Deletion of 3:")
# tree.inorder_traversal()
# print()


# matrix = [[10, 20, 30, 100], [40, 50, 60, 110], [70, 80, 90, 120]]
# transpose_matrix = []
# for j in range(len(matrix[0])):
#     lst = []
#     for i in matrix:
#         lst.append(i[j])
#     transpose_matrix.append(lst)

# print(transpose_matrix)

# transpose_matrix1 = [[i[j] for i in matrix]for j in range(len(matrix[0]))]
# print(transpose_matrix1)
        