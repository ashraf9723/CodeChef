# cook your dish here
t = int(input())

for _ in range(t):
    
    x,y  = map(int,input().split())
    
   # Calculate the points scored by Chef
    work_hr= y-x
   
    print(work_hr)