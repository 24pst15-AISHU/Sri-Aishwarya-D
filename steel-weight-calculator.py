# Reinforcement Steel Weight Calculator
# Used in civil engineering to calculate steel weight

print("Steel Weight Calculator")

diameter = float(input("Enter bar diameter (mm): "))
length = float(input("Enter length of bar (m): "))
number = int(input("Enter number of bars: "))

# Formula: Weight = (D^2 / 162) × Length × Number
weight = (diameter ** 2 / 162) * length * number

print("\nTotal Steel Weight =", round(weight,2), "kg")
