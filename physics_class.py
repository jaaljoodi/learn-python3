# Variables
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# A function called f_to_c that takes
# an input f_temp, a temperature in Fahrenheit,
# and converts it to Celsius.
def f_to_c(f_temp):
  return (f_temp - 32) *5/9

# Tests the above function with a value of 100 Fahrenheit.
f100_in_celsius = f_to_c(100)

# A function called c_to_f that takes
# an input c_temp, a temperature in Celsius
# and converts it to Fahrenheit
def c_to_f(c_temp):
  return (c_temp * 9/5) + 32

# Tests your function with a value of 0 Celsius
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# A function takes in mass and acceleration.
# returns mass multiplied by acceleration
def get_force(mass, acceleration):
  return mass * acceleration

# Tests the function above
train_force = get_force(train_mass, train_acceleration)
print(train_force)

# Prints "The GE train supplies 226800 Newtons of force"
print("The GE train supplies " + str(train_force) + " Newtons of force")

# A function that takes mass and C
def get_energy(mass, c=3*10**8):
  return mass * c **2

# Tests the function above
bomb_energy = get_energy(bomb_mass)

# Prints "A 1kg bomb supplies 90000000000000000 Joules"
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")

# A function that takes mass, acceleration, distance
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

# Tests the function above
train_work = get_work(train_mass, train_acceleration, train_distance)

# Prints "The GE train does 22680000 Joules of work over 100 meters"
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters")
