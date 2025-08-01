# # Q1 = find_dupllicates in arr containing values from 1 to n
# arr =  [2, 3, 1, 2, 1]
# def find_duplicates(arr):
#     n = len(arr)
#     duplicates = []
#     for i in range(n):
#         index = arr[i] % n
#         arr[index] += n
#     for i in range(n):
#         if arr[i] // n > 1:
#             duplicates.append(i)
#     return duplicates 

# print(find_duplicates(arr))


# # Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# # An input string is valid if:

# # Open brackets must be closed by the same type of brackets.

# # Open brackets must be closed in the correct order.

# # Every close bracket has a corresponding open bracket of the same type.

# str = '({[[]]})'

# # def valid_parantheses(str):
# #     stack = []
# #     for char in str:
# #         if char in '({[':
# #             stack.append(char)
# #         elif char == ')':
# #             if not stack or stack[-1] != '(':
# #                 return False
# #             stack.pop()
# #         elif char == ']':
# #             if not stack or stack[-1] != '[':
# #                 return False
# #             stack.pop()
# #         elif char == '}':
# #             if not stack or stack[-1] != '{':
# #                 return False
# #             stack.pop()
# #     return len(stack) == 0

# def valid_parantheses(str):
#     stack = []
#     mappings = {')' : '(', '}' : '{', ']': '['}
#     for ch in str:
#         if ch in mappings.values():
#             stack.append(ch)
#         elif ch in mappings.keys():
#             if not stack or stack[-1] != mappings[ch]:
#                 return False
#             stack.pop()
#     return len(stack) == 0 

# print(valid_parantheses(str))


# #LONGEST PALINDROME SUBSTRING
# str = 'abaxyzzyxf'

# def expand_around_centre(str, left, right):
#     n = len(str)
#     while left >= 0 and right < n and str[left] == str[right]:
#         left -= 1
#         right += 1
#     return str[left + 1 : right]

# def longest_palindrome_substring(str):
#     n = len(str)
#     if n == 0:
#         return ''
#     longest = ''
#     for i in range(n):
#         #odd length palindrome
#         odd_palindrome = expand_around_centre(str, i, i)
#         # even length palindrome
#         even_palindrome = expand_around_centre(str, i, i + 1)

#         if len(odd_palindrome) > len(longest):
#             longest = odd_palindrome
#         if len(even_palindrome) > len(longest):
#             longest = even_palindrome
#     return longest

# print(longest_palindrome_substring(str))

#next smaller element
# arr = [2, 1, 4, 3]

# def next_smaller_optimised(arr):
#     stack = [-1]
#     n = len(arr)
#     ans = [-1] * len(arr)
#     for i in range(n-1, -1,-1):
#         while stack and stack[-1] > arr[i]:
#             stack.pop()
#         if stack:
#             ans[i] = stack[-1]
#         stack.append(arr[i])
#     return ans


# def next_smaller_element(arr):
#     ans = [-1] * len(arr)
#     for i in range(len(arr) - 1):
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[i]:
#                 ans[i] = arr[j]
#                 break
#     return ans

# print(next_smaller_element(arr))
# print(next_smaller_optimised(arr))



# # previous smaller element
# arr = [2, 1, 4, 3]


# def previous_smaller_optimised(arr):
#     stack = [-1]
#     ans = [-1] * len(arr)

#     for i in range(len(arr)):
#         while stack and stack[-1] >= arr[i]:
#             stack.pop()
#         if stack:
#             ans[i] = stack[-1]
#         stack.append(arr[i])
    
#     return ans


# def previous_smaller_element(arr):
#     ans = [-1] * len(arr)

#     for i in range(1, len(arr)):
#         for j in range(i-1, -1, -1):
#             if arr[j] < arr[i]:
#                 ans[i] = arr[j]
#                 break
    
#     return ans

# print(previous_smaller_element(arr))
# print(previous_smaller_optimised(arr))


# # # next smaller element with index 
# arr = [2, 1, 4, 0]

# def next_smaller_element_with_index(arr):
#     stack = [-1]
#     ans = [-1] * len(arr)
#     for i in range(len(arr) - 1, -1, -1):
#         while stack and arr[stack[-1]] >= arr[i]:
#             stack.pop()
#         if stack:
#             ans[i] = stack[-1]
#         stack.append(i)
#     return ans

# print(next_smaller_element_with_index(arr))


# largest rectangle area in histogram
# heights = [2,1,5,6,2,3]

# def largest_rectangle_area(heights):
#     n = len(heights)
#     max_area = 0
#     for i in range(n):
#         length = heights[i]
#         width = 1
#         j = i - 1
#         while j >= 0 and heights[j] >= length:
#             width += 1
#             j -= 1

#         k = i + 1
#         while k < n and heights[k] >= length:
#             width += 1
#             k += 1

#         area = length * width
#         max_area = max(max_area, area)
#     return max_area

# print(largest_rectangle_area(heights))

# def next_smaller_number(heights):
#     stack = [-1]
#     ans = [-1] * len(heights)
#     for i in range(len(heights) - 1 , -1, -1):
#         while stack and heights[stack[-1]] >= heights[i]:
#             stack.pop()
#         if stack:
#             ans[i] = stack[-1]
#         stack.append(i)
#     return ans
    
# def prev_smaller_number(heights):
#     stack = [-1]
#     n = len(heights)
#     ans = [-1] * n
#     for i in range(n):
#         while stack and heights[stack[-1]] >= heights[i]:
#             stack.pop()
#         if stack:
#             ans[i] = stack[-1]
#         stack.append(i)
#     return ans

# def largest_area_rectangle_optmised(heights):
#     n = len(heights)
#     next = next_smaller_number(heights)
#     print(next)
#     prev = prev_smaller_number(heights)
#     print(prev)
#     print(heights)
#     max_area = float('-inf')
#     for i in range(n):
#         length = heights[i]
#         if next[i] == -1:
#             next[i] = n
#         width = next[i] - prev[i] - 1
#         area = length * width 
#         max_area = max(max_area, area)
#     return max_area

# print(largest_area_rectangle_optmised(heights))


# #print permutations of string
# str = 'abc'

# def solve_rec(str , ans, temp):
#     if len(str) == 0:
#         ans.append(temp)
#         return
#     for i in range(len(str)):
#         curr_char = str[i]
#         rem_char = str[: i] + str[i+1:]
#         solve_rec(rem_char, ans, temp + curr_char)

# def print_permutations(str):
#     ans = []
#     solve_rec(str, ans, '')
#     return ans

# print(print_permutations(str))



# print substring of a given str
# str = 'abc'
# def find_substring(str):
#     res = []
#     for i in range(len(str)):
#         for j in range(i, len(str)):
#             res.append(str[i : j + 1])
#     return res
# res = find_substring(str)
# print(res)


### sliding window problem


# # Maximum Subarray Sum Of Size K
# arr = [2, 4, 15, 1, 10, 2, 6]
# k = 3

# def max_subarray_sum(arr, k):
#     max_sum = float('-inf')
#     i = 0
#     sum = 0
#     for j in range(len(arr)):
#         sum += arr[j]
#         if j - i + 1 == k:
#             max_sum = max(max_sum ,sum)
#             sum = sum - arr[i]
#             i+=1
#     return max_sum

# print(max_subarray_sum(arr, k))



# # # First Negative number in every window size k
# arr = [-8, -2, 3, -6, 10, -2, 5]
# k = 3

# def first_negative_number(arr, k):
#     ans_lst = []
#     i = 0
#     temp = []
#     for j in range(len(arr)):
#         if arr[j] < 0: 
#             temp.append(arr[j])
#         if j - i + 1 == k:
#             if len(temp) == 0:
#                 ans_lst.append(0)
#             else:
#                 ans_lst.append(temp[0])
#                 if arr[i] == temp[0]:
#                     temp.pop(0)
#             i+=1
#     return ans_lst

# print(first_negative_number(arr, k))


# ## count occurence of anagrams 

# str = 'aaaa'
# pattern = 'aaba'

# def count_anagram_occurence(str, pattern):
#     map = {}
#     for char in pattern:
#         if char in map.keys():
#             map[char] += 1
#         else:
#             map[char] = 1
#     count = len(map)
#     k = len(pattern)
#     i = 0
#     ans = 0
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
#                 map[str[i]] += 1
#             i += 1
#     return ans  
    

# print(count_anagram_occurence(str, pattern))  

            

# # # maximum of all subarray of size k
# arr = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3

# def max_of_all_subarray(arr, k):
#     temp = []
#     ans = []
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
# def max_of_all_subarray_optimised(arr, k):
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


# print(max_of_all_subarray(arr, k))



# # # minimum of all subarray of size k
# arr = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3

# from collections import deque
# def min_of_all_subarray_optimised(arr, k):
#     queue = deque()
#     i = 0
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

# print(min_of_all_subarray_optimised(arr, k))
    

# # # largest Subarray of Sum K with all value positive

# arr = [10, 5, 1, 4, 1, 9]
# k = 15

# def largest_subarray_length_for_sum_K(arr , k):
#     sum = 0
#     maxi = 0
#     start_index = 0
#     end_index = 0
#     i = 0
#     for j in range(len(arr)):
#         sum += arr[j]
#         while sum > k and i <= j:
#             sum -= arr[i]
#             i += 1
#         if sum == k:
#             length = j - i + 1
#             if length > maxi:
#                 maxi = length
#                 start_index  = i
#                 end_index = j + 1
#     print(arr[start_index: end_index])

#     return maxi

# print(largest_subarray_length_for_sum_K(arr, k))


# # largest Subarray of Sum K with all values positive and negative 

# arr = [-1, 3, 10, 1, 5, 7, 1, -6, 9]
# k = 1

# def largest_subarray_sum(arr, k):
#     prefix_sum_map = {0:-1} # really essential if subarray start from 0th index 
#     prefix_sum = 0
#     maxi = 0
#     start_index = -1
#     end_index = -1
#     for j in range(len(arr)):
#         prefix_sum += arr[j]
#         if prefix_sum - k in prefix_sum_map:
#             length =  j - prefix_sum_map[prefix_sum - k]
#             if length > maxi:
#                 maxi = length
#                 start_index = prefix_sum_map[prefix_sum - k] + 1
#                 end_index = j
#         if prefix_sum not in prefix_sum_map:
#             prefix_sum_map[prefix_sum] = j
#     if start_index != -1:
#         print("Subarray:", arr[start_index:end_index + 1])
#     else:
#         print("No subarray found")
#     return  maxi

# print(largest_subarray_sum(arr, k))



# # # Find the longest substring with k unique characters in a given string
# str = "aabacbebebe"
# k = 3
# def longest_substring_with_K_char(str, k):
#     maxi = float('-inf')
#     map = {}
#     start_index = -1
#     end_index = -1
#     i = 0
#     for j in range(len(str)):
#         if str[j] in map:
#             map[str[j]] += 1
#         else: 
#             map[str[j]] = 1
#         while len(map) > k and i <= j:
#             map[str[i]] -= 1
#             if map[str[i]] == 0:
#                 map.pop(str[i])
#             i += 1
#         if len(map) == k:
#             length = j - i + 1
#             if length > maxi:
#                 maxi = length
#                 start_index = i
#                 end_index = j + 1

#     print('substring: ', str[start_index:end_index])
#     return maxi
# print(longest_substring_with_K_char(str, k))


# # # Find the longest substring with without repeating characters in a given string
# str = "pwwkew"

# def longest_substring_without_repeating_char(str):
#     map = {}
#     start_index = -1
#     end_index = -1
#     i = 0
#     maxi = -1
#     for j in range(len(str)):
#         if str[j] in map:
#             map[str[j]] +=1
#         else:
#             map[str[j]] = 1
#         while len(map) < j - i + 1 and i <= j:
#             map[str[i]] -= 1
#             if map[str[i]] == 0:
#                 map.pop(str[i])
#             i += 1
#         if len(map) == j -i + 1:
#             length = j - i + 1
#             if length > maxi:
#                 maxi = length
#                 start_index = i
#                 end_index = j + 1
#     print('string is :', str[start_index:end_index])
#     return maxi

# print(longest_substring_without_repeating_char(str))


# # # leetcode 904. Fruit Into Baskets

# fruits = [1,2,3,2,2]

# def fruits_in_baskets(fruits):
#     k = 2
#     maxi = -1
#     i = 0
#     map = {}
#     for j in range(len(fruits)):
#         if fruits[j] in map:
#             map[fruits[j]] +=1 
#         else :
#             map[fruits[j]] = 1
#         while len(map) > k and i <= j:
#             map[fruits[i]] -= 1
#             if map[fruits[i]] == 0:
#                 map.pop(fruits[i])
#             i += 1
#         maxi = max(maxi, j - i + 1)

#     return maxi

# print(fruits_in_baskets(fruits))



# # # Minimum Window Sustring
# str = 'this is a test string'
# pattern = 'tist'

# def minimum_window_substring(s, pattern):
#     if not s or not pattern:
#         return ''

#     freq_map = {}
#     for char in pattern:
#         freq_map[char] = freq_map.get(char, 0) + 1

#     i = 0
#     min_len = float('inf')
#     min_start = 0
#     count = len(freq_map)

#     for j in range(len(s)):
#         if s[j] in freq_map:
#             freq_map[s[j]] -= 1
#             if freq_map[s[j]] == 0:
#                 count -= 1

#         while count == 0:
#             if j - i + 1 < min_len:
#                 min_len = j - i + 1
#                 min_start = i

#             if s[i] in freq_map:
#                 freq_map[s[i]] += 1
#                 if freq_map[s[i]] > 0:
#                     count += 1
#             i += 1

#     if min_len == float('inf'):
#         print("No valid window")
#         return ''
#     else:
#         print('string is :', s[min_start:min_start + min_len])
#         return min_len   

# print(minimum_window_substring(str, pattern))


# # # KADANE'S algorithm for Largest Sum Contiguous array
# arr = [-2,-3,4,-1,-2,1,5,-3]

# # def kadane_algo(arr):
# #     curr_sum = 0
# #     max_sum = arr[0]
# #     for num in arr:
# #         curr_sum += num
# #         max_sum = max(max_sum, curr_sum)
# #         if curr_sum < 0 :
# #             curr_sum = 0
# #     return max_sum

# # print(kadane_algo(arr))

# def kadane_algo_with_arr(arr):
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
#     max_subarray = arr[start: end + 1]
#     return max_sum, max_subarray

# max_sum, subarray = kadane_algo_with_arr(arr)
# print(max_sum)
# print(subarray)


# #transpose matrix
# matrix = [[10, 20, 30, 100], 
#           [40, 50, 60, 110], 
#           [70, 80, 90, 120]]
# transpose_matrix = []

# #for columns traversal
# for i in range(len(matrix[0])):
#     temp_lst = []
#     # for row traversal
#     for j in range(len(matrix)):
#         temp_lst.append(matrix[j][i])
#     transpose_matrix.append(temp_lst)
# print(transpose_matrix)


# # merge sort
# arr = [-2,-4,4,-1,2,1,5,-3]

# def merge(left ,right):
#     sorted_arr = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             sorted_arr.append(left[i])
#             i += 1
#         else:
#             sorted_arr.append(right[j])
#             j += 1
#     if i < len(left):
#         while i < len(left):
#             sorted_arr.append(left[i])
#             i+=1
#     if j < len(right):
#         while j < len(right):
#             sorted_arr.append(right[j])
#             j+=1
#     return sorted_arr

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid  = len(arr)//2
#     left_arr = merge_sort(arr[:mid])
#     right_arr = merge_sort(arr[mid:])

#     return merge(left_arr, right_arr)

# print(merge_sort(arr))

# arr = [-2,-4,4,-1,2,1,5,-3]

# def merge(arr, left, mid, right, temp):
#     i, j, k = left, mid + 1, left
#     while i <= mid and j <= right:
#         if arr[i] < arr[j]:
#             temp[k] = arr[i]
#             i += 1
#         else:
#             temp[k] = arr[j]
#             j += 1
#         k += 1

#     while i <= mid:
#         temp[k] = arr[i]
#         i += 1
#         k += 1

#     while j <= right:
#         temp[k] = arr[j]
#         j += 1
#         k += 1

#     for index in range(left, right + 1):
#         arr[index]  = temp[index]

# def merge_sort_helper(arr, left, right, temp):
#     if left < right:
#         mid = (left + right) // 2
#         merge_sort_helper(arr, left, mid, temp)
#         merge_sort_helper(arr, mid + 1, right , temp)
#         merge(arr, left, mid, right, temp)

# def merge_sort_optimised(arr):
#     temp = [0] * len(arr)
#     merge_sort_helper(arr, 0, len(arr) - 1, temp)

# merge_sort_optimised(arr)
# print(arr)


# #quick sort
# arr = [-2,-4,4,-1,2,1,5,-3]
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[-1]
#     left = []
#     right = []
#     equal = []

#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num > pivot:
#             right.append(num)
#         else:
#             equal.append(num)

#     return quick_sort(left) + equal + quick_sort(right)

# print(quick_sort(arr))


# def partition(arr, low, high):
#     pivot  = arr[high]
#     i = low - 1
#     for j in range(low, high):
#         if arr[j] < pivot:
#             i+=1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i+1], arr[high] = arr[high] ,arr[i + 1]

#     return i + 1


# def quick_sort_inplace(arr, low, high):
#     if low < high:
#         pivot_index = partition(arr, low,high)
#         quick_sort_inplace(arr, low, pivot_index - 1)
#         quick_sort_inplace(arr, pivot_index + 1, high)

# quick_sort_inplace(arr, 0, len(arr) - 1)
# print(arr)




# ########### target sum for 3 numbers ##########

# arr = [1,8,4,2,9,11,3]
# target_sum = 15

# def solve_target_sum(arr, target_sum):
#     arr.sort()#[1, 2, 3, 4, 8, 9, 11]
#     n = len(arr)
#     for i in range(0, n - 2):   
#         j = i + 1
#         k = n - 1
#         while j < k:
#             if arr[i]+arr[j] + arr[k] == target_sum:
#                 print(arr[i], arr[j], arr[k])
#                 j+=1
#                 k-=1
#             elif arr[i] + arr[j] + arr[k] > target_sum:
#                 k -= 1
#             else:
#                 j+=1
                

# solve_target_sum(arr, target_sum)


# You are working as a receptionist and you receive a list of all the meetings scheduled for the next day.
#  Each meeting has a start and end time, and there is only one meeting room available. 
# Your task is to schedule the maximum number of non-overlapping meetings in that room. How would you approach this problem?"


# start_times = [9, 9.5, 10, 11, 11.5, 12]
# end_times   = [10, 12, 11, 12, 13, 14]

# def max_meetings(start_times, end_times):
#     n = len(start_times)

#     meetings = []
#     for i in range(n):
#         meetings.append((start_times[i], end_times[i]))

#     meetings.sort(key= lambda x: x[1])

#     selected_meetings = []
#     last_end_time = float('-inf')

#     for start, end in meetings:
#         if start >= last_end_time:
#             selected_meetings.append((start, end))
#             last_end_time = end
#     return selected_meetings


# result  = max_meetings(start_times, end_times)

# print("Maximum number of non-overlapping meetings:", len(result))
# print("Scheduled meetings (start, end):", result)


################################################two pointer problems###################################################################
# Problem: Given a sorted array, find a pair with a specific sum.

# Example: Input: [1, 2, 3, 4, 6], target = 6 → Output: [1, 3]
# arr =  [1, 2, 3, 4, 4, 6]
# target = 6
# def target_sum_pair(arr, target):
#     i = 0
#     j = len(arr) - 1
#     while i < j:
#         sum = arr[i] + arr[j]
#         if sum < target:
#             i+=1
#         elif sum > target:
#             j-=1
#         else:
#             print(i, j)
#             j-=1
#     return i, j

# target_sum_pair(arr, target)    


# # Problem: Remove duplicates in-place from a sorted array.

# # Input: [1, 1, 2, 3, 3] → Output: [1, 2, 3]
# arr = [1, 1, 2, 2, 3, 3]

# def remove_duplicates(arr):
#     i = 0
#     for j in range(1, len(arr)):
#         if arr[i] != arr[j]:
#             i+=1
#             arr[i] = arr[j]
#     return i + 1, arr[: i + 1]
# length, unique_arr = remove_duplicates(arr)
# print(f"Length: {length}, Unique Array: {unique_arr}")
    

# # Problem: Move all zeros to the end while maintaining the order.

# # Input: [0, 1, 0, 3, 12] → Output: [1, 3, 12, 0, 0]

# arr = [0, 1, 0, 3, 12]

# def move_zero_to_end(arr):
#     i = 0
#     for j in range(len(arr)):
#         if arr[j] > 0:
#             arr[i], arr[j] = arr[j], arr[i]
#             i+=1
#     return arr            

# print(move_zero_to_end(arr))


# # Valid Palindrome

# # Problem: Check if a string is a palindrome, ignoring non-alphanumeric.

# str = "A man, a plan, a canal: Panama"

# def valid_palindrome(str):
#     str = str.lower()
#     # str = str.replace(',','').replace(' ', '').replace(':','')
#     # print(str)
#     str_1 = ''
#     for char in str:
#         if char.isalnum():
#             str_1 += char
#     i = 0
#     j = len(str_1) - 1
#     while i < j:
#         if str_1[i] != str_1[j]:
#             return False
#         i+=1
#         j-=1
#     return True
# print(valid_palindrome(str))


# # Squares of a Sorted Array

# # Problem: Return a new array with squares of each number sorted.

# # Input: [-2, -1, 0, 2, 3] → Output: [0, 1, 4, 4, 9]

# arr = [-2, -1, 0, 2, 3]

# def sorted_squares(arr):
#     n = len(arr)
#     left = 0
#     right  = n - 1
#     pos = n - 1
#     ans_arr = [0] * n
#     while left <= right:
#         if abs(arr[left]) > abs(arr[right]):
#             ans_arr[pos] = arr[left] ** 2
#             left += 1
#         else:
#             ans_arr[pos] = arr[right] ** 2
#             right -= 1
#         pos -= 1
#     return ans_arr

# print(sorted_squares(arr))



# 3Sum

# Problem: Find all triplets in the array that sum up to 0.

# Input: [-1, 0, 1, 2, -1, -4] → Output: [[-1, -1, 2], [-1, 0, 1]]

# arr = [-1, 0, 1, 2, -1, -4]

# def find_triplets(arr):
#     arr.sort()
#     res = []
#     for i in range(len(arr)):
#         if i > 0 and arr[i] == arr[i - 1]:
#             continue
#         left = i + 1
#         right  = len(arr) - 1
#         while left < right:
#             curr_sum = arr[i] + arr[left] + arr[right]
#             if curr_sum == 0:
#                 res.append([arr[i], arr[left], arr[right]])

#                 while left < right and arr[left] == arr[left + 1]:
#                     left +=1
#                 while left < right and arr[right] == arr[right - 1]:
#                     right -= 1
#                 left +=1
#                 right -= 1
#             elif curr_sum > 0:
#                 right -= 1
#             else:
#                 left += 1
#     return res


# print(find_triplets(arr))

# Container With Most Water

# Problem: Find two lines that together with the x-axis form a container with the most water.

# Input: [1,8,6,2,5,4,8,3,7] → Output: 49


# arr = [1,8,6,2,5,4,8,3,7]

# def maximum_water_tank(arr):
#     i = 0
#     j = len(arr) - 1
#     maxi = float('-inf')
#     start_index = 0
#     end_index = 0 
#     while i < j:
#         curr_cap = min(arr[i], arr[j]) * (j - i)
#         if curr_cap > maxi:
#             maxi  = curr_cap
#             start_index = i
#             end_index = j
#         if arr[i] < arr[j]:
#             i+=1
#         else :
#             j-=1
#     return maxi , arr[start_index : end_index + 1]

# cap, ans= maximum_water_tank(arr)
# print('maximum capacity is :', cap)
# print('x -axis index are: ', ans)


# Subarray Product Less Than K

# Problem: Count subarrays where the product is less than k.

# Input: [10, 5, 2, 6], k = 100 → Output: 8

# arr = [10, 5, 2, 6]
# k = 100
# def count_subarray(arr, k):
#     count  = 0
#     for i in range(len(arr)):
#         curr = 1
#         temp = []
#         for j in range(i, len(arr)):
#             curr =  curr * arr[j]
#             temp.append(arr[j])
#             if curr < k: 
#                print(temp)
#                count +=1
#             elif curr >= k:
#                 break   
#     return count 

# print(count_subarray(arr, k))

# arr = [10, 5, 2, 2, 4]
# k = 100
# def count_subarray_optimised(arr, k):
#     prod = 1
#     left = 0
#     count = 0
#     for right in range(len(arr)):
#         prod  = prod * arr[right]
#         while prod >= k:
#             prod  = prod // arr[left]
#             left +=1
#         count += right - left + 1
#     return count 

# print('optimised approach : ', count_subarray_optimised(arr, k))


# # Longest Substring with At Most k Distinct Characters
# # Input: s = "aabacbebebe", k = 3
# # Output: 7

# str = 'aabacbebebe'
# k = 3
# def longest_substring_with_k_char(str, k):
#     i = 0
#     start_index = -1
#     end_index = -1
#     maxi = float('-inf')
#     fmap = {}
#     for j in range(len(str)):
#         fmap[str[j]] = fmap.get(str[j], 0) + 1
#         if len(fmap) == k:
#             str_len =  j - i + 1
#             if str_len > maxi:
#                 start_index = i
#                 end_index = j
#                 maxi = str_len
#         while len(fmap) > k:
#             if str[i] in fmap:
#                 fmap[str[i]] -= 1
#                 if fmap[str[i]] == 0:
#                     fmap.pop(str[i])
#             i+=1
#     return maxi, str[start_index: end_index + 1]

# print(longest_substring_with_k_char(str, k))


# Longest Substring Without Repeating Characters
# Input: "abcabcbb" → Output: 3

# # str = 'abcabcbb'
# str = 'pwwkew'
# def longest_substring_without_repeating_char(str):
#     i = 0
#     start_index = -1
#     end_index = -1
#     maxi = float('-inf')
#     fmap = {}
#     for j in range(len(str)):
#         fmap[str[j]] = fmap.get(str[j], 0) + 1
#         while len(fmap) < j - i + 1:
#             fmap[str[i]] -= 1
#             if fmap[str[i]] == 0:
#                 fmap.pop(str[i])
#             i += 1
#         if len(fmap) == j - i + 1:
#             str_len = j - i + 1
#             if str_len > maxi:
#                 maxi = str_len
#                 start_index = i
#                 end_index = j
                
#     return maxi, str[start_index: end_index + 1]

# print(longest_substring_without_repeating_char(str))


# # Minimum Window Substring

# # Problem: Find the smallest substring in s that contains all characters of t.

# # s = "zoomlazapzo"
# # p = "oza"
# s = "timetopractice"
# p = "toc"

# def min_window_substring(str, pattern):
#     fmap = {}
#     for char in pattern:
#         fmap[char] = fmap.get(char, 0) + 1
#     count  = len(fmap)
#     i = 0
#     start_index = -1
#     end_index = -1
#     mini = float('inf')
#     for j in range(len(str)):
#         if str[j] in fmap:
#             fmap[str[j]] -= 1
#             if fmap[str[j]] == 0:
#                 count -= 1
#         while count  == 0:
#             str_len = j - i + 1
#             if str_len < mini:
#                 mini = str_len
#                 start_index = i
#                 end_index = j
#             if str[i] in fmap:
#                 fmap[str[i]] +=1
#                 if fmap[str[i]] > 0:
#                     count +=1
#             i+=1
#     return mini, str[start_index: end_index +1]

# print(min_window_substring(s, p))

# # Shortest Subarray with Sum K

# # arr = [2, 4, 6, 10, 2, 1]
# # k = 12 

# arr = [-8, -8, -3, 8]
# k = 5 

# def shortest_subarray_sum_k(arr, k):
#     prefix_sum_map = {0: -1}
#     prefix_sum = 0
#     mini = float('inf')
#     start_index = -1
#     end_index = -1
#     for j in range(len(arr)):
#         prefix_sum  = prefix_sum + arr[j]
#         if prefix_sum  - k in prefix_sum_map:
#             arr_len = j - prefix_sum_map[prefix_sum - k] 
#             if mini > arr_len:
#                 mini = arr_len
#                 start_index = prefix_sum_map[prefix_sum - k] + 1
#                 end_index = j
#         if prefix_sum not in prefix_sum_map:
#             prefix_sum_map[prefix_sum] = j
#     if start_index == -1:
#         return -1, [] 
#     return mini, arr[start_index: end_index + 1]

# print(shortest_subarray_sum_k(arr, k))


# # shortest subarray with sum atleast K
# # arr = [2, -1, 2]
# # k = 3 
# arr = [2, 1, 1, -4, 3, 1, -1, 2]
# k = 5

# def shortest_subarray_naive(arr, k):
#     mini = float('inf')

#     for i in range(len(arr)):
#         curr_sum = 0
#         count  = 0
#         for j in range(i, len(arr)):
#             count += 1
#             curr_sum += arr[j]
#             if curr_sum >= k:
#                 if count < mini:
#                     min_start = i
#                     min_end = j
#                     mini  = count 
#     if mini == float('inf'):
#         return -1
#     return mini, arr[min_start: min_end + 1]
# print(shortest_subarray_naive(arr, k))



# Longest Mountain in Array

# Problem: Find the longest "mountain" (increasing then decreasing) in an array.


# # Trapping Rain Water

# # Problem: Calculate trapped water between bars using two pointers.

# # Input: [0,1,0,2,1,0,1,3,2,1,2,1] → Output: 6

# arr = [0,1,0,2,1,0,1,3,2,1,2,1]
# def trapping_rain_water_naive(arr):
#     ans = 0
#     for i in range(1, len(arr) - 1):
#         left = arr[i]
#         for j in range(i):
#             left = max(left, arr[j])
#         right = arr[i]
#         for j in range(i + 1, len(arr)):
#             right = max(right, arr[j])
#         ans += (min(left, right) - arr[i])
#     return ans


# print(trapping_rain_water_naive(arr))


# def trapping_rainwater_optimised(arr):
#     left = 1
#     right = len(arr) - 2
#     lmax = arr[left - 1]
#     rmax = arr[right + 1]
#     res = 0
#     while left <= right:
#         if lmax <= rmax:
#             res += max(0, lmax - arr[left])
#             lmax = max(lmax, arr[left])
#             left += 1
#         else:
#             res += max(0, rmax - arr[right])
#             rmax = max(rmax ,arr[right])
#             right -= 1
#     return res 
# arr = [2, 1, 5, 3, 1, 0, 4]
# print(trapping_rainwater_optimised(arr))

#longest mountain##

# def longest_mountain(arr):
#     ans = 0
#     for i in range(len(arr)):
#         j = i + 1
#         inc = 0
#         dec = 0
#         #check for increment
#         while j < len(arr) and arr[j] > arr[j - 1]:
#             j += 1
#             inc = 1
#         # check for decrement
#         while j < len(arr) and arr[j] < arr[j - 1]:
#             j += 1
#             dec = 1
#         if inc and dec:
#             if ans < j - i:
#                 ans = j - i
#                 start_index = i
#                 end_index = j
#     return ans, arr[start_index : end_index]
# arr = [1, 3, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5]
# print(longest_mountain(arr))

# def longest_mountain_optimised(arr):
#     if len(arr) < 3:
#         return 0
#     mon_start = -1

#     ans  = 0
#     i = 1
#     while i <= len(arr) - 2:
#         if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
#             left = i
#             right  = i
#             while left > 0 and arr[left - 1] < arr[left]:
#                 left -= 1
#             while right < len(arr) - 1 and arr[right] > arr[right + 1]:
#                 right +=1
#             length = right - left + 1
#             if length > ans:
#                 ans  = length 
#                 mon_start = left
#                 mon_end = right
#             i = right
#         else:
#             i += 1
#     if mon_start == -1:
#         print("No mountain found.")
#         return 0, []

#     return ans, arr[mon_start: mon_end + 1]

# print(longest_mountain_optimised(arr))

# 4Sum

# Problem: Find all quadruplets that sum to a target value.

# Input: [1, 0, -1, 0, -2, 2], target = 0

# arr = [1, 0, -1, 0, -2, 2]
# target = 0
# def four_sum(arr, target):
#     arr.sort()
#     n = len(arr)
#     res = []
#     for i in range(n - 3):
#         if i > 0 and arr[i] == arr[i - 1]:
#             continue
#         for j in range(i + 1, n - 2):
#             if j > i + 1 and arr[j] == arr[j - 1]:
#                 continue
#             left = j + 1
#             right = n - 1
#             while left < right:
#                 curr_sum = arr[i] + arr[j] + arr[left] + arr[right]
#                 if curr_sum == target:
#                     res.append([arr[i], arr[j], arr[left], arr[right]])

#                     while left < right and arr[left] == arr[left + 1]:
#                         left += 1
#                     while left < right and arr[right] == arr[right - 1]:
#                         right -= 1
#                     left += 1
#                     right -= 1
                
#                 elif curr_sum > target:
#                     right -= 1
#                 else:
#                     left += 1
#     return res
# print(four_sum(arr, target))


# m = 4
# n = 5

# matrix = [[0] * n for _ in range(m)]

# num = 1
# for col in range(n):
#     if col % 2 == 0:
#         for row in range(m):
#             matrix[row][col] = num
#             num += 1
#     else:
#         for row in reversed(range(m)):
#             matrix[row][col] = num
#             num += 1

# for row in matrix:
#     print(row)

# m = 4
# n = 5
# output
# 1 8 9  16  17
# 2 7 10 15 18
# 3 6 11 14 19
# 4 5 12 13 20


## prefix sum pattern questions


# # Running Sum of 1d Array
# # arr = [1,2,3,4]
# arr = [1,1,1,1,1]

# def running_sum(arr):
#     ans_arr = []
#     prefix_sum = 0
#     for i in range(len(arr)):
#         prefix_sum += arr[i]
#         ans_arr.append(prefix_sum)
#     return ans_arr
# print(running_sum(arr))


# find pivot index leetcode 724

# nums = [1,7,3,6,5,6]

# def find_pivot_index(arr):
    
#     n = len(arr)
#     for i in range(n):
#         left = i - 1
#         right = i + 1
#         l_sum = 0
#         r_sum = 0
#         while left >= 0:
#             l_sum += arr[left]
#             left -= 1
#         while right < n:
#             r_sum += arr[right]
#             right += 1
#         if l_sum == r_sum:
#             return i
# find_pivot_index(nums)


# def find_pivot_index_optimised(arr):
#     total_sum = 0
#     for num in arr:
#         total_sum += num
#     left_sum = 0
#     for i in range(len(arr)):
#         right_sum = total_sum - left_sum - arr[i]
#         if left_sum == right_sum:
#             return i
#         left_sum += arr[i]
#     return -1

# print(find_pivot_index_optimised(nums))



# Subarray Sum Equals K (small inputs) – Leetcode #560

nums = [1,2,3]
k = 3
# def subarray_sum_equals_k(arr, k):
#     count = 0
#     res_arr = []
#     for i in range(len(arr)):
#         curr_sum = 0
#         for j in range(i , len(arr)):
#             curr_sum += arr[j]
#             if curr_sum == k:
#                 count += 1
#                 res_arr.append(arr[i:j + 1])
#     return count, res_arr

# print(subarray_sum_equals_k(nums, k))

# # nums = [1,1,1]
# # k = 2
# nums = [1, -1, 2, 3, -2, 2]
# k = 3
# def subarry_sum_equals_k_optimised(arr, k):
#     p_map = {0 : 1}
#     curr_sum = 0
#     count  = 0
#     for num in arr:
#         curr_sum += num
#         if curr_sum - k in p_map:
#             count += p_map[curr_sum - k]
#         # if curr_sum in p_map:
#         #     p_map[curr_sum] += 1
#         # else:
#         #     p_map[curr_sum] = 1
#         p_map[curr_sum] = p_map.get(curr_sum, 0) + 1
        
#     return count 

# print(subarry_sum_equals_k_optimised(nums, k))


# Contiguous Array – Leetcode #525

# # nums = [0, 1, 0]
# nums  = [0,1,1,1,1,1,0,0,0]
# def contiguous_array(arr):
#     for i in range(len(arr)):
#         if arr[i] == 0:
#             arr[i] = -1
#     # after changing all 0 to -1 we have to find maximum subarray where sum is 0
#     k = 0
#     p_map = {0: -1}
#     prefix_sum = 0
#     max_length = 0
#     start_index = -1
#     for j in range(len(arr)):
#         prefix_sum += arr[j]
#         if prefix_sum - k in p_map:
#             length  = j - p_map[prefix_sum - k]
#             if length > max_length:
#                 start_index = p_map[prefix_sum - k] + 1
#                 max_length = length
#         else:
#             p_map[prefix_sum] = j
#     return max_length, [1 if x == 1 else 0 for x in arr[start_index: start_index + max_length]]

# print(contiguous_array(nums))


# Matrix Block Sum – Leetcode #1314
# dry run krna chiye

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
k = 1
# def matrix_block_sum(matrix, k):
#     m = len(matrix)
#     n = len(matrix[0])
#     res_arr = [[0] * n for _ in range(m)]

#     for i in range(m):
#         for j in range(n):
#             curr_sum = 0
#             for row in range(max(0, i - k),min(m, i + k + 1)):
#                 for col in range(max(0, j - k), min(n, j + k + 1)):
#                     curr_sum += matrix[row][col]
#             res_arr[i][j] = curr_sum
#     return res_arr

# res_arr = matrix_block_sum(matrix, k)
# for row in res_arr:
#     print(row)


# def matrix_block_sum_optimised(matrix, k):
#     m = len(matrix)
#     n = len(matrix[0])

#     pre_matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

#     for i in range(m):
#         for j in range(n):
#             pre_matrix[i + 1][j + 1] = matrix[i][j] + pre_matrix[i][j + 1] + pre_matrix[i + 1][j] - pre_matrix[i][j]
        
#     ans_matrix = [[0 for _ in range(n) ]for _ in range(m)]

#     for i in range(m):
#         for j in range(n):
#             r1 = max(0, i - k)
#             c1 = max(0, j - k)
#             r2 = min(m - 1, i + k)
#             c2 = min(n - 1, j + k)
#             ans_matrix[i][j] = pre_matrix[r2 + 1][c2 + 1] - pre_matrix[r1][c2 + 1] - pre_matrix[r2 + 1][c1] + pre_matrix[r1][c1]
#     return ans_matrix

# ans = matrix_block_sum_optimised(matrix, k)

# for row in ans:
#     print(row)



# # Range Sum Query - Immutable – Leetcode #303
# from typing import List
# import time
# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.nums  = nums

#     def sumRange(self, left: int, right: int) -> int:
#         curr_sum = 0
#         for i in range(left, right + 1):
#             curr_sum += self.nums[i]

#         return curr_sum
#     def pre_sum_calculate(self):
#         ans_arr = [0] * len(self.nums)
#         ans_arr[0] = self.nums[0]
#         for i in range(1, len(self.nums)):
#             ans_arr[i] = self.nums[i] + ans_arr[i - 1]
#         return ans_arr
#     def sum_range_optimised(self, left, right, pre_sum):
#         if left == 0:
#            return pre_sum[right]
#         return pre_sum[right] - pre_sum[left - 1]

# # Your NumArray object will be instantiated and called as such:
# nums = [1, 2, 3, 4]
# obj = NumArray(nums)
# pre_sum = obj.pre_sum_calculate()
# start = time.time()
# print(obj.sumRange(1, 3))
# print(obj.sumRange(0, 3))
# print(obj.sumRange(1, 2))
# end = time.time()
# print("Time for basic sumRange:", end - start)

# start = time.time()
# print("after optimisation:")
# print(obj.sum_range_optimised(1, 3, pre_sum))
# print(obj.sum_range_optimised(0, 3, pre_sum))
# print(obj.sum_range_optimised(1, 2, pre_sum))
# end = time.time()
# print("Time for optimised sum:", end - start)


###################
#  Maximum Sum of 3 Non-Overlapping Subarrays – Leetcode #689
# arr = [1, 2, 1, 2, 6, 7, 5, 1]
# k = 2
# arr = [1, 2, 1, 2, 6, 7, 5, 1, 6, 7, 5]
# k = 3
# def maximum_sum_of_3_non_overlapping_subarray(arr, k):
#     max_sum = float('-inf')
#     n = len(arr)
#     ans_arr = []
#     for i in range(n - 3 * k + 1):
#         for j in range(i + k, n - 2 * k + 1):
#             for l in range(j + k, n - k + 1):
#                 # curr_i = 0
#                 # curr_j = 0
#                 # curr_l = 0
#                 # for index in range(k):
#                 #     curr_i += arr[i + index]
#                 #     curr_j += arr[j + index]
#                 #     curr_l += arr[l + index]
#                 curr_i = sum(arr[i: i + k])
#                 curr_j = sum(arr[j: j + k])
#                 curr_l = sum(arr[l: l + k])
#                 total_sum = curr_i + curr_j + curr_l
#                 # print(f'i is {i}, j is {j},  l is {l}, curr[i] is {curr_i},  curr[j] is {curr_j},  curr[l] is {curr_l}, and total_sum is {total_sum}')
#                 # print(total_sum)
#                 if total_sum > max_sum:
#                     max_sum = total_sum
#                     ans_arr = [i, j, l]
#                 if total_sum == max_sum and [i, j, l] < ans_arr:
#                     ans_arr = [i, j, l]
#     return max_sum, ans_arr 
# print(maximum_sum_of_3_non_overlapping_subarray(arr , k))

# def maximum_sum_of_3_non_overlapping_subarray_optimised(arr, k):
#     window_sum = [sum(arr[i : i + k])for i in range(len(arr) - k + 1)]
#     m = len(window_sum)
#     # array contains index of maxium value in window_sum from left to right
#     left_arr = [0] * m
#     best = 0
#     for i in range(m):
#         if window_sum[i] > window_sum[best]:
#             best  = i
#         left_arr[i] = best
#     #array contains index of maximum value in window_sum from right to left
#     right_arr = [0] * m
#     best = m - 1
#     for j in range(m - 1, -1, -1):
#         if window_sum[j] >= window_sum[best]:
#             best = j
#         right_arr[j] = best
    
#     ans_arr = []
#     max_total = float('-inf')

#     for i in range(k, m - k):
#         j = left_arr[i - k]
#         l = right_arr[i + k]
#         total = window_sum[i] + window_sum[j] + window_sum[l]
#         if total > max_total:
#             max_total = total
#             ans_arr = [j, i, l]
#     return max_total, ans_arr
    

# print(maximum_sum_of_3_non_overlapping_subarray_optimised(arr, k))


# Count of Range Sum – Leetcode #327
# nums = [-2, 5, -1]
# lower = -2
# upper = 2
# def count_range_sum_naive(arr, lower, upper):
#     ans_cnt = 0
#     for i in range(len(arr)):
#         curr_sum = 0
#         for j in range(i, len(arr)):
#             curr_sum += arr[j]
#             if  lower <= curr_sum <= upper:
#                 ans_cnt += 1
#     return ans_cnt

# print(count_range_sum_naive(nums, lower, upper))


####questions asked in uber
# we have to find minimum time maria takes to cook all dishes
# n = 5
# dishinfo = [
#     [2, 4],   # Dish 1: takes 2 min, must finish by 4
#     [1, 9],   # Dish 2: takes 1 min, must finish by 9
#     [1, 8],   # Dish 3: takes 1 min, must finish by 8
#     [4, 9],   # Dish 4: takes 4 min, must finish by 9
#     [3, 12]   # Dish 5: takes 3 min, must finish by 12
# ]

# def minimum_time_to_serve_all_dishes(n, dishinfo):
#     #sort the dishes by deadline
#     dishinfo.sort(key = lambda x: x[1])
#     curr_time = 0
#     for x, y in dishinfo:
#         curr_time += x # x time to cook , y = deadline
#         if curr_time > y:
#             return -1 # deadline missed
#     return curr_time

# print(minimum_time_to_serve_all_dishes(n, dishinfo))


### maximum no of meetings we can have in one meeting room
# start_times = [9, 9.5, 10, 11, 11.5, 12]
# end_times   = [10, 12, 11, 12, 13, 14]


# def max_meetings(start_times, end_times):
#     meetings = []
#     n = len(start_times)
#     for i in range(n):
#         meetings.append([start_times[i], end_times[i]])
#     meetings.sort(key = lambda x : x[1])
#     last_end_time = float('-inf')
#     selected_meetings = []
#     for start, end in meetings:
#         if start >= last_end_time:
#             selected_meetings.append([start, end])
#             last_end_time = end
#     return selected_meetings
    
# result = max_meetings(start_times, end_times)
# print('the meetings which we can schedule are:', result)
# print('no of meetings which we can schedule are:', len(result))


#### max_trains_on_one_platform
# arr_time = [900, 940, 950, 1100, 1500, 1800]
# dep_time = [910, 1200, 1120, 1130, 1900, 2000]
# arr_time = [900, 1235, 1100]
# dep_time = [1000, 1240, 1200]
# def max_trains_on_one_platform(arr_time, dep_time):
#     n = len(arr_time)
#     scheduling = []
#     for i in range(n):
#         scheduling.append([arr_time[i], dep_time[i]])
#     scheduling.sort(key = lambda x: x[1])

#     max_trains = 0
#     last_end_time = float('-inf')
#     for start, end in scheduling:
#         if start >= last_end_time:
#             last_end_time = end
#             max_trains += 1
#     return max_trains

# print(max_trains_on_one_platform(arr_time, dep_time))

### minimum platform needed two pointer approach
# arr_time = [900, 940, 950, 1100, 1500, 1800]
# dep_time = [910, 1200, 1120, 1130, 1900, 2000]

# def minimum_platform_needed(arr_time, dep_time):
#     arr_time.sort()
#     dep_time.sort()
#     n = len(arr_time)
#     i = j = 0
#     plat_needed = max_platform = 0

#     while i < n:
#         if arr_time[i] < dep_time[j]:
#             plat_needed += 1
#             i += 1
#         else:
#             plat_needed -= 1
#             j += 1
#         max_platform = max(max_platform, plat_needed)
#     return max_platform
    

# # #### min no of meeting room needed to schedule all meetings
# start_times = [9, 9.5, 10, 11, 11.5, 12]
# end_times   = [10, 12, 11, 12, 13, 14]

# def minimum_no_of_meeting_rooms(start_times, end_times):
#     start_times.sort()
#     end_times.sort()
#     n = len(start_times)
#     max_rooms = 0
#     room_need = 0
#     i = j = 0
#     while i < n:
#         if start_times[i] < end_times[j]:
#             room_need += 1
#             i += 1
#         else:
#             room_need -= 1
#             j += 1
#         max_rooms = max(max_rooms, room_need)
#     return max_rooms

# print(minimum_no_of_meeting_rooms(start_times, end_times))



# ###prime number
# def is_prime(num):
#     if num <= 1:
#         return False
#     end = int(num**0.5)
#     for i in range(2, end + 1):
#         if num % i == 0:
#             return False
#     return True
    
# n = 100
# for i in range(0, n+1):
#     if is_prime(i):
#         print(i, end=' ')

####longest common prefix

# def longest_common_prefix(strs):
#     if len(strs) == 0:
#         return 'empty list'
#     prefix = ''
#     for i in range(len(strs[0])):
#         curr_char = strs[0][i]
#         for s in strs[1:]:
#             if i >= len(s) or curr_char != s[i]:
#                 return prefix
#         prefix += curr_char
#     return prefix

# strs = ["flower", "flow", "flight"]
# print(longest_common_prefix(strs))


# ### encyrpt and decrypt a string
# original_str = 'Hello World'

# def encrypt_fun(str, shift):
#     encrypted = ''
#     for ch in str:
#         if ch.isalpha():
#             base = ord('A') if ch.isupper() else ord('a')
#             encrypted +=  chr((ord(ch) - base + shift)%26 + base)
#         else:
#             encrypted += ch
#     return encrypted
# encrypted_str = encrypt_fun(original_str, 3)
# print(encrypted_str)
# decrypted_str = encrypt_fun(encrypted_str, -3)
# print(decrypted_str)

### decorator example

# def log_decorator(func):
#     def wrapper(*args):
#         print('Car is of black color')
#         func(*args)
#         print('Going to kashmir')
#     return wrapper


# @log_decorator
# def drive(car_name):
#     print(f'Driving the 4X4 {car_name}')

# drive('THAR')


####generator example
# def generator_fun():
#     for i in range(5):
#         yield i

# gen = generator_fun()
# print(next(gen))
# print(next(gen))
# print(next(gen))

# for num in generator_fun():
#     print(num)


# def fibonacci_nums(limit):
#     a, b = 0, 1
#     count = 0
#     while count<limit:
#         print(a, end= " ")
#         a, b = b, a+b
#         count += 1

# fibonacci_nums(10)


############OOPS
#class
#class is the blue print of an object
#object
# Object is the instance of a class
#methods

# class Car:
#     engine = 'MAHINDRA' #class attribute
#     def __init__(self, car_name, price):
#         self.car_name = car_name
#         self.price = price
#     # instance method
#     def fetch_car_details(self, name):
#         name = name.upper()
#         if name == self.car_name:
#             return {'car_name':self.car_name,'price': self.price, 'engine': self.engine}
#         else:
#             return 'No car found with this name.'
#     # static method 
#     @staticmethod
#     def is_affordable(price):
#         return price < 25

# thar = Car('THAR', 20)
# details = thar.fetch_car_details('Thar')
# print(details)
# print('IS this  car afforadabe:',thar.is_affordable(20))
# scorpio = Car('SCORPIO', 30)
# details = scorpio.fetch_car_details('ScorPio')
# print(details)
# print('IS this  car afforadabe:',scorpio.is_affordable(20))

# inheritence
# inherit some features from parent and add some more feature in child class 
# class Vechile:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def display_info(self):
#         return f'Brand: {self.brand}, Model: {self.model}'
# class Car(Vechile):
#     def __init__(self, brand, model, fuel_type):
#         super().__init__(brand, model)
#         self.fuel_type = fuel_type
#     # method overriding
#     def display_info(self):
#         return f'{super().display_info()}, Fuel : {self.fuel_type}'
# class Bike(Vechile):
#     def __init__(self, brand, model, engine_cc):
#         super().__init__(brand, model)
#         self.engine_cc = engine_cc
#     # Extends parent's method
#     def display_info(self):
#         return f"{super().display_info()}, Engine: {self.engine_cc}cc"
    
# car = Car('Mahindra', 'THAR', 'petrol')
# bike = Bike('Royal Enfield', 'classic 350', 350)

# print(car.display_info()) 
# print(bike.display_info()) 
# encapsulation
## hiding the internal state of an object use private, protected variables
# class BankAccount:
#     def __init__(self, owner, balance, account_type):
#         self.owner = owner
#         self.__balance = balance #private variable 
#         self._account_type = account_type
#     def __validate_amount(self, amount):
#         return amount > 0
#     def deposit(self, amount):
#             if self.__validate_amount(amount):
#                 self.__balance += amount
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#     def get_balance(self):
#         return self.__balance
#     def get_account_type(self):
#         return self._account_type
    
#     def set_account_type(self, new_account_type):
#         new_account_type = new_account_type.lower()
#         if new_account_type in ['saving', 'current']:
#             self._account_type = new_account_type
#         else:
#             print('invalid account type.')


# account1 = BankAccount('abc', 10000, 'saving')
# account1.deposit(1000)
# account1.withdraw(2000)
# print(f'available balance for {account1.owner} is:',account1.get_balance())
# print(f'account type for {account1.owner} is : {account1.get_account_type()}')
# print('setting new account type.')
# account1.set_account_type('Current')
# print(f'account type for {account1.owner} is : {account1.get_account_type()}')


# abstraction
#focus in hiding complex implementation details and expose only essentiual features of an object
# # same example we can use abstract method
# from abc import ABC, abstractmethod

# class PaymentProcessor(ABC):
#     @abstractmethod
#     def process_payment(self, amount):
#         pass
#     @abstractmethod
#     def refund_payment(self, amount):
#         pass
# class CreditCardProcessor(PaymentProcessor):
#     def process_payment(self, amount):
#         print(f"Processing credit card payment of ${amount}")
#         return True
#     def refund_payment(self, amount):
#         print(f"Refunding ${amount} to credit card")
#         return True
# class PayPalProcessor(PaymentProcessor):
#     def process_payment(self, amount):
#         print(f"Processing PayPal payment of ${amount}")
#         return True
#     def refund_payment(self, amount):
#         print(f"Refunding ${amount} via PayPal")
#         return True

# def checkout(processor: PaymentProcessor, amount):
#     if processor.process_payment(amount):
#         print('Payment Successfull')
#     else:
#         print('Payment Failed')

# credit_card = CreditCardProcessor()
# paypal = PayPalProcessor()

# checkout(credit_card, 100)
# checkout(paypal, 50)

# polymorphism
# types of polymorphirsm
# 1. method overriding (runtime polymorphism)
# 2. method overloading(compile time polymorphism)
# class Car:
#     def move(self):
#         return 'Driving on Road'
# class Boat:
#     def move(self):
#         return 'Sailing on Water'
# class Airplane:
#     def move(self):
#         return 'Flying in the air'

# vechiles = [Car(), Boat(), Airplane()]

# for vechile in vechiles:
#     print(vechile.move())

# ### polymorphism with abstract base class
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#      #must implement the area method(abstract) by child class
#     def area(self):
#         return 3.14 * self.radius ** 2
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     #must implement the area method(abstract) by child class
#     def area(self):
#         return 4 * self.side 

# shapes = [Circle(5), Square(4)]
# for shape in shapes:
#     print(shape.area())         

#composition
# composition is a design principle where a class contains objects of other classes as members, 
# rather then inherit from them. it represent has-a relation 
# class Engine:
#     def start(self):
#         print('Engine Started')
#     def stop(self):
#         print('Engine Stopped')
# class Wheels:
#     def rotate(self):
#         print('Wheel rotating')

# class Car:
#     def __init__(self):
#         self.engine = Engine()# composition has a relationship
#         self.wheels = [Wheels() for _ in range(4)]
    
#     def drive(self):
#         self.engine.start()
#         for wheel in self.wheels:
#             wheel.rotate()
#         print('car is moving')

# my_car = Car()
# my_car.drive()

# ### dunder methods or magic methods
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#     # String representation for print() and str()
#     def __str__(self):
#         return f"{self.title} by {self.author}"
    
#     def __len__(self):
#         return self.pages
#     # Official string representation (used by repr())
#     def __repr__(self):
#         return f"Book: {self.title}, {self.author}, {self.pages}"
    
#     def __del__(self):
#         print('A book object has been deleted.')
    
# book = Book('book1', 'author1', 302)
# print(str(book))
# print(len(book))
# print(repr(book))
# del book

    

