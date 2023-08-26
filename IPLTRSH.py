# cook your dish here
t = int(input())

for _ in range(t):
    
    n,m  = map(int,input().split())
    
    
    if n>m:
        go = n-m
        print(go)
    else:
         print("0")