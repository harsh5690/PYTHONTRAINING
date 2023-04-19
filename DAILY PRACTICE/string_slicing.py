str="androidpython"
print(len(str))

#display starting 3 characters froma existing string - string slicing
#note : string index always start froma 0

print(str[:3])

#display last 3 characters

print(str[-3:])

#display last charator from string
print(str[-1])

#display middle charator from string 

print(str[5])

#reverse string 
print(str[::])# it will form by default index 0 index and end with default index ending index
print(str[::-1])# it will reverse order print

# add to new string

s2 = str[:3] + "hello" + str[-3:]
print(s2)