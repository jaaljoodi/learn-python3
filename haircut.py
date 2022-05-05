# calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Create a variable total_price, and set it to 0.
total_price = 0


# Loop through the prices list and add 
# each price to the variable total_price
# it should sum up all the prices of haircuts
for price in prices:
  total_price += price


# create a variable called average_price
# that is the total_price divided by the number of prices.
average_price = price
print('Average Haircut Price:', average_price)


# Use a list comprehension to make a list
# called new_prices, which has each element
# in prices minus 5.
new_prices = [price - 5 for price in prices]
print(new_prices)

# Create a variable called total_revenue
# and set it to 0.
total_revenue = 0

# Prints out the total total_revenue of last week
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print('Total Revenue:', total_revenue)

# Find the average daily revenue by dividing
# total_revenue by 7
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# Use a list comprehension to create a
# list called cuts_under_30
cuts_under_30 = [new_prices[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)
