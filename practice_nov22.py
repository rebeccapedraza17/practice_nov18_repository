# Rebecca Pedraza
# Nov 22

def string_splosion(str):
    #Function needs to return on exploded version of the string given
    exploded = " "
    for i in range(len(str)):
        exploded += str[:i]
    return exploded + str
print (string_splosion)

'''
def string_splosion(str):
    for i in range(len(str)):
        if i % 2 == 0:
            result += str[i]

'''
'''
my_str = "This is a test"
print(my_str[11])

string_splosion("hello") 
string_splosion("code")
string_splosion("abc")
'''
