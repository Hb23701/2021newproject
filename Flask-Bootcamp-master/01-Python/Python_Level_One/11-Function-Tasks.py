# Function Tasks
#
#
# Let's see if you can solve these word problems by creating functions.
# The function "skeleton" has been set up for you to fill in below the problem
# description, as well as example outputs of what the function should return
# given certain inputs. Best of luck, some of these will be challenging!
#
# The tasks will start off easy and proceed to get harder and harder.

# ## Task 1
#
#  Create a function that takes in two integers and returns
## a Boolean True if their sum is 10, False if their sum is something else.

# def check_ten(n1,n2):
#     return n1+n2 

# result = check_ten(1,9)

# if result == 10:
#     print ("True")
# else:
#     print("False")




# ## Task 2

# # Create a function that takes in two integers and returns True if their
# # sum is 10, otherwise, return the actual sum value.

# def check_ten_sum(n1,n2):
#     return n1+n2

# result = check_ten_sum(5,6)

# if result == 10:
#     print("True")
# else:
#     print (result)



# # ## Task 3
# #
# # Create a function that takes in a string and returns back the
# # first character of that string in upper case.
# def first_upper(mystring):
#     return mystring[0].upper()

# print(first_upper("hello"))


## Task 4

# Create a function that takes in a string and returns the last two characters.
# If there are less than two chracters, return the string:  "Error".
# Use this link if you need help/hint.
# (https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string)



# def last_two(mystring):
#     if len(mystring)>2:
#         return mystring[-2:]
#     else:
#         return "Error"
    
    

# print(last_two("hello"))

# print(last_two("he"))




# ## Task 5

# # Given a list of integers, return True if the sequence [1,2,3] is somewhere
# # in the list. Hint: Use slicing and a for loop.



def seq_check(nums):
    for n in nums:
        for number in [1,2,3]:
            if n == number:
                return True
            else:
                return False

print(seq_check([2,3,1,4,5,6]))
print(seq_check([1,2,3,1,4,5,6]))
print(seq_check([5,6,7,1,2,3,4,5,6]))
# ## Task 6
#
# Given a 2 strings, create a function that returns the difference in length
# between them. This difference in length should always be a positive number
# (or just 0). Hint: Absolute Value.**



def compare_len(s1,s2):
    return abs(len(s2)-len(s1))

print(compare_len("abc","ab"))
print (compare_len("hello","goodbye"))



# # ## Task 7
# #
# # Given a list of integers, if the length of the list is an even number,
# # return the sum of the list. If the length of the list is odd, return the max
# ## value in that list.



def sum_or_max(mylist):
    if len(mylist)%2 == 0:
        return sum(mylist)
    else:
        return max(mylist)

print(sum_or_max([1,2]))
print(sum_or_max([1,2,3,4]))