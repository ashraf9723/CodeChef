def final_balance(initial_balance, deposit, deduction, months):
    return initial_balance + (deposit - deduction) * months

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read input values for each test case
    initial_balance, deposit, deduction, months = map(int, input().split())
    
    # Calculate the final account balance
    balance = final_balance(initial_balance, deposit, deduction, months)
    
    # Print the final balance
    print(balance)
