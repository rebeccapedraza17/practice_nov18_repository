# Rebecca Pedraza
# Nov 15

# Write a function called unique_squares(list_nums)
# That returns the squares of all the numbers in the list
# Without any repeats

'''
squares = (["2","7","13","9"])

def unique_squares(list_num):
    squares = []
    squares.append(i * 2)
    
def unique_squares(list_nums):
    squares = []
    for i in list_nums:
        squares.append(i*2)
    return squares
'''

def unique_squares(nums):
    squared = []
    for num in nums:
        if num*num not in squared:
            squared.append(num*num)
    return squared

def unique_squares_but_bad(nums):
    return [num*num for num in set(nums)]
