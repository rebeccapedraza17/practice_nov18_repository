# Rebecca Pedraza
# Nov 7

def check_within_ten(num):
    
    # I need to compare num with 100
    # If num -100 is between 0 and 10
    # If is within 10 or 100
    # Or if num -100 is between 0 and -10
    # If is within 10 or 100
    
    if (num - 100 <= 10) and (num - 100 >= -10):
    # Other way to do it 
    #  (10 >= num - 100 >= -10):
        within_ten = True
    else:
        within_ten = False
    return within_ten
    
print(check_within_ten(73))
print(check_within_ten(95))
print(check_within_ten(103))
print(check_within_ten(117))

'''
# Other way to do it less times
def check_within_ten(num):
    if (num - 100 <= 10) and (num - 100 >= -10):
        check_within_ten(num)
    return True
'''

