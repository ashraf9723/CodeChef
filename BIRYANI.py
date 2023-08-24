# cook your dish here
t = int(input())
for _ in range(t):
    
    x,y = map(int,input().split())
    
    # calculate the total cost
    total_cost = x*y
    
    print(total_cost)