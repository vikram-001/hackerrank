'''
Task 
Read an integer N.
Without using any string methods, try to print the following:
123...N
Note that "..." represents the values in between.
'''

N = int(input())
for x in range(1,N+1) :
    print(x,end = "")