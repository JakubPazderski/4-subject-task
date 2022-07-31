x=input("Wpisz słowo, które chcesz sprawdzić:")
def check_the_word(x):
    """Function cheks if 
    reversed string 
    is the same 
    as original string"""
    return x==x[::-1]
"""Assigning a function
to the variable 'answer'"""
answer=check_the_word(x)
print(bool(answer))
"""I hope everything is OK! :)"""    