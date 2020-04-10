t=int(input())
for _ in range(t):
    s=list(input())
    even=[] 
    odd=[]   
    for i in range(len(s)):
        if i%2==0:
            even.append(s[i])
        if i%2!=0:
            odd.append(s[i])      
    print(''.join(even)+" "+''.join(odd))
