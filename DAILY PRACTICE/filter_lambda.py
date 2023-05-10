"""
filter() method filters the given sequence with the help of function which test each elements in the sequnce

snytax :

fliter(function,seqence)

function: function which tests if each elements of a sequence is true or not
sequence : sequence which needs to filter and store list or tuple
"""
sequence = ['a','e','i','f','u','l']
def mylogic(alphabet):
    vowel_list = ['a','e','i','u']
    if alphabet in vowel_list:
        return True
    else :
        return False
    
filtered_data = filter(mylogic,sequence)

for i in filtered_data:
    print(i)