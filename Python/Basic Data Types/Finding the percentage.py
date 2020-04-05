#Sample Input:
'''
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika'''
#Sample Output:
'56.00'


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        #student_marks[name] = scores                       #Original Stub code : Gives output list of marks [52,56,60]
        student_marks[name] = sum(scores)/len(scores)       #Here sum(scores)/len(scores) Directly stores the avg of scores of each student in student_marks
    query_name = input()
print("%0.2f" %student_marks[query_name])                   #Hence due to reasons in previous comment we simply call the key of dict whic is associated with avg marks of each student i.e {'Malika' = 56.00}
#print(student_marks)                                       #Check to print entire dict
