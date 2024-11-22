'''
# Rebecca Pedraza
# Nov 12

# Ask user for two numbers
number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))

# Print the larger of the two numbers
# Create a function called find_max(a,b)
# That function will return the larger of two numbers

if number1 > number2:
    print(f"{number1} is bigger")
else:
    print(f"{number2} is bigger (or they are equal)")
    
'''

# More practice with data types
def find_max(a,b):
    if a > b:
        return a
    return b 

def return_top_two(a,b,c):
    temp = [a, b, c]
    sort(temp)
    return temp[1], temp[2] 

best, next_best = return_top_two(5,78,2)

top = return_top_two(3245,56,133525464)
