# cook your dish here
t = int(input())

for _ in range(t):
    
    x,h  = map(int,input().split())
    
    if x<h:
        print("NO")
    elif x>=h:
        print("YES")
    