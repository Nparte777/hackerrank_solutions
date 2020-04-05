if __name__ == '__main__':
   l = []
   for _ in range(int(input())):                                #iterating input() with forced int convert
       l.append([input(), float(input())])                      #appending two values as 1 element in list l as : [['name',score],['name',score]]
   #print(l)
   sh = sorted(set(x[1] for x in l))                            #create sorted list sh based on score alone where x[1] is Score in l
   #print(sh)
   for name in sorted(x[0] for x in l if x[1] == sh[1]):        #iterate over x[0] in l which is the name part of list elements ['name',score] if x[1](socre) == x[1] from sored sh list
       print(name)
