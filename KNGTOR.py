# cook your dish here
t = int(input())

for _ in range(t):
    
    x,n  = map(int,input().split())
    
   # Calculate the points scored by Chef
    sit = x*5+n*7
    
    # Print the result for the current test case
    print(sit)