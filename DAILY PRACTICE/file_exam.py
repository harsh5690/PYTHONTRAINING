f = open("terms.txt","r")
#print(f.read())                 
l1 = f.readlines()
print(len(l1))
for i in l1:
    print(i)