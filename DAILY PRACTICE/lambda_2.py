#write a python program find odd number using lambda.

sequence = [1,2,3,4,5,6,7,8,9,10]
def mylogic(odd_numbers):
    if odd_numbers%2 == 0:
        return True
    else :
        return False
    
filtered_data = filter(mylogic,sequence)

for i in filtered_data:
    print(i)