# Define a weight variable and set it equal to any number.
weight = 8
# Create a variable for the cost of ground shipping.
cost_ground = 0

# Ground shipping.

# Create an if/elif/else statement for the cost of ground shipping. 
# It should check for weight, and print the cost of shipping a package
# of that weight.
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 20 + 3.00
elif weight > 5 and weight <= 10:
  cost_ground = weight * 20 + 4
elif weight > 10:
  cost_ground = weight * 20 + 4.75
print("Ground shipping is: $" + str(cost_ground))

# Create a variable for the cost of premium ground shipping.
prem_cost = 125
print("Ground Shipping Premium is: $" + str(prem_cost))

# Drone Shipping.
drone_shipping = 0

# Create an if/elif/else statement for the cost of drone shipping. 
# It should check for weight, and print the cost of shipping a package
# of that weight.
if weight <= 2:
  drone_shipping = weight * 4.50
elif weight > 2 and weight <= 6:
  drone_shipping = weight * 9.00
elif weight > 5 and weight <= 10:
  drone_shipping = weight * 12.00
elif weight > 10:
  drone_shipping = weight * 14.00
print("Drone shipping is: $" + str(drone_shipping))