# cook your dish here
t = int(input())

for _ in range(t):
    
    x,n  = map(int,input().split())
    if x>=n:
      print("YES")
    else:
        print("NO")