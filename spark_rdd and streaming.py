







# Q1 = find_dupllicates in arr containing values from 1 to n
arr =  [2, 3, 1, 2, 3, 1]
def find_duplicates(arr):
    n = len(arr)
    duplicates = []
    for i in range(n):
        index = arr[i] % n
        arr[index] += n
    for j in range(n):
        if arr[j] //n >1:
            duplicates.append(j)
    return duplicates

# print(find_duplicates(arr))




# Q2 = sort arr of 0 and 1 only
arr = [1,1,0,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0]

def sort01(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] == 0:
            left += 1
        elif arr[right] == 1:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
 
# sort01(arr)
# print(arr)


# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.

# Open brackets must be closed in the correct order.

# Every close bracket has a corresponding open bracket of the same type.

str = '({[[]]})'

# def valide_parentheses(str):
#     stack = []
#     for ch in str:
#         if ch == '(' or ch == '{' or ch == '[':
#              stack.append(ch)
#         elif ch == ')':
#             if not stack or stack[-1] != '(':
#                 return False
#             stack.pop()
#         elif ch == '}':
#             if not stack or stack[-1] != '{':
#                   return False
#             stack.pop()
#         elif ch == ']':
#             if not stack or stack[-1] != '[':
#                 return False
#             stack.pop()
#     if len(stack) == 0:
#          return True
#     else:
#          return False
    
def valide_parentheses(str):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for ch in str:
        if ch in mapping.values():
            stack.append(ch)
        elif ch in mapping.keys():
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
    return len(stack) == 0
	
# Test cases

valide_test_cases = [
    "",                  # Empty string
    "({[]})",            # Nested mixed brackets
    "()[]{}",            # Multiple valid sequences
    "(((((((((())))))))))",  # Deeply nested brackets
    "()" * 10000         # Long balanced string
]

invalid_test_cases = [
	"(((",                          # Only open brackets
	"))}",                          # Only close brackets
	"({[})]",                       # Incorrect closing order
	"[([])]",                       #matched brackets
	"(",                            # Single open bracket
	"([)]",                         # Wrong close type
	"(" * 10000 + ")" * 9999,       # Long unbalanced string
	")" + "()" * 10000              # Early mismatch in long string
]
 
# for str in valide_test_cases:
#     print(valide_parentheses(str))
# for str in invalid_test_cases:
# 	print(valide_parentheses(str))
# print(valide_parentheses(str))



# longest palindrome substring

str = 'abaxyzzyxf'
# str = 'abaac'

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

def longest_palindrome_substring(str):
    n = len(str)
    if n == 0:
        return ""
    longest = ""
    for i in range(n):
        odd_palindrome = expand_around_center(str, i, i)
        # print('odd_palindrome',odd_palindrome)
        even_palindrome = expand_around_center(str, i, i + 1)
        print('even_palindrome',even_palindrome)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    return longest

print(longest_palindrome_substring(str))



