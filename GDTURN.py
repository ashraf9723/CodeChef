# cook your dish here
def is_goodturn(x,y):
    if(x+y)>6:
        print("Yes")
    else:
        print("No")
        
    t = int(input())
    for _ in range(t):
        x,y = map(int,input().split())
        result =is_goodturn(x,y)
        print(result)