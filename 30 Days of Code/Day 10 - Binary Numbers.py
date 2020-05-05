n = int(input())
y=bin(n)
#print(y)               #Output is 0bbinary number ex. 0b101
list1=y[2:]             #To remove 0b
#print(list1)
list2="".join(list1).split("0")
lt3=[]
for i in list2:
    lt3.append(i.count("1"))
print(max(lt3))
