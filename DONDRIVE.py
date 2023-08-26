# cook your dish here
t = int(input())

for _ in range(t):
    
    n,x  = map(int,input().split())
    
   # Calculate the points scored by Chef
    points_scored = n-x
    
    # Print the result for the current test case
    print(points_scored)