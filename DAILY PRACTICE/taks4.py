# enter 5 subject marks and total marks

l1 = []

for i in range(1,6):
    mark = int(input("enter mark : "))
    l1.append(mark)

print(sum(l1))