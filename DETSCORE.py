# cook your dish here
t = int(input())

for _ in range(t):
    
    x,n  = map(int,input().split())
    
   # Calculate the points scored by Chef
    points_scored = (x * n) // 10
    
    # Print the result for the current test case
    print(points_scored)