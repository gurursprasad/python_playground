# Prime nuumber
# n = 6

# if n <= 1:
#     print("Not a prime number")
# else:
#     is_prime = True
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print("It's a prime number")
#     else:
#         print("Not a prime number")



# # Given a string, find the longest substring that does not contain any repeated characters
# s = "abcdabcbb"

# char_set = set()
# l = 0
# result = 0

# for r in range(len(s)):
#     while s[r] in char_set:
#         char_set.remove(s[l])
#         l += 1
#     char_set.add(s[r])
#     result = max(result, r-l + 1)

# print(result)

# Minumum size subarray sum
nums = [2,3,1,2,4,3] # op = 2
target = 7

left = 0
right = 0
result = 99999999999999999999999
sub_sum = 0 # Store the sum of aub arrays

while right < len(nums):
    sub_sum += nums[right]
    
    while sub_sum >= target: # After adding the sub sum and it becomes equal to or greater than target, we have to move the left pointer to right and this will reduce the sub_sum
        result = min(result, right-left+1)        
        sub_sum -= nums[left]
        left += 1

    right += 1

print(result)
