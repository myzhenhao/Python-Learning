# input and output
# string

print("Welcome, what is your name? ")
my_name = input()
print("Welcome, how old are you? ")
my_age = input()
print(f"Welcome, {my_name} is {my_age}")


# integer

apple_price = 3
orange_price = 4
print("Welcome to my store")
print(f"Apple is RM{apple_price}")
print(f"Orange is RM{orange_price}")
print(f"How many apple do you want?")
apple_input = int(input())
print(f"How many orange do you want?")
orange_input = int(input())
total_apple = apple_input * apple_price
total_orange = orange_input * orange_price
total_fruits = total_apple + total_orange
print(f"total apple price is RM{total_apple}")
print(f"total apple price is RM{total_orange}")
print(f"total for all fruits is RM{total_fruits}")
