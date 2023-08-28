def can_beat_einstein(initial_iq):
    final_iq = initial_iq + 7
    return final_iq > 170

# Read the input
initial_iq = int(input())

# Check if Chef can beat Einstein
if can_beat_einstein(initial_iq):
    print("Yes")
else:
    print("No")