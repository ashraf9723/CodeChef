# cook your dish here
t = int(input())

for _ in range(t):
    
    A,B = map(int,input().split())
    
    # Calculate the maximum number of burgers Chef can make
    max_burgers = min(A,B)
    
    # Print the result for the current test case
    print(max_burgers)