# cook your dish here
# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read Alice's and Bob's heights
    x, y = map(int, input().split())
    
    # Compare heights and print the result
    if x > y:
        print("A")
    else:
        print("B")
       
    
  