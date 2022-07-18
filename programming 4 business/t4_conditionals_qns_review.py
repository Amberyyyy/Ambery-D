# 1 
# For each of the following expressions, fill in the blank
# (indicated by __) with an appropriate Boolean comparator so that 
# the expression evaluates to True: 

# print(4 _ 2)

# print(5 _ 10)

# print("python" _ "C++")

# print(50 _ "50")


# 2
# Add parentheses where necessary so that each of the following 
# expressions evaluates to True:

# print(False == not True)

# print(True and False == True and False)

# print(not True and "A" == "B")


# 3 
# Write a conditional statement to evaluate if the school variable contains `business and accountancy`. 
# If the evaluation is true, print `business and accountancy`, else print `invalid entry`.

school = "business and accountancy"


# 4 
# Write a conditional statement to evaluate the price of an apple and orange. 
# If the price of apple is greater than orange, print "apple price is higher than orange". 
# If the price of apple is greater than orange, print "apple price is lower than orange". 
# Otherwise, print "apple and orange prices are equal" 

# Test your conditions by assigning different values to 2 variables, example:
apple_price = 0.74
orange_price = 0.74

# 5
# Write a conditional statement to evaluate the following conditions of a variable `height`:
# If height is greater or equal to 175, print "tall"
# If height is greater or equal to 165 and less than 175, print "average"
# If height is less than 165, print "short"
# Test the condition with 160, 170 and 180 to evaluate the conditional statements, example:

height = 170

# 6 
# Write a conditional statement to evaluate the following conditions: 
    # gender == "female" and hair_length == "long", print "tie up your hair"
    # gender == "female" and hair_length == "short", print "style your hair"
    # gender == "male" and hair_length == "long", print "cut your hair"
    # gender == "male" and hair_length == "short", print "comb your hair"

# Test the conditions to evaluate the conditional statement, example:
gender = "male" 
hair_length = "long"

# 7
# Write a `for loop` to iterate over range(21) to evaluate each value of the range function
# with the following conditions:

    ## value == 1, print (f"{value} is first value")
    ## value == 10 , print (f"{value} is middle value")
    ## value == 20, print (f"{value} is last value")

# When the program is executed, it should display the output:
    ## 1 is first value
    ## 10 is middle value
    ## 20 is last value

# 8 
# Create a for loop to iterate over enumerate(range(80, 150)).
# In each loop, print the index (coming from enumerate() function) and value (coming from range() function) 
# Break the iteration when the index reach number 20.

# 9 
# Create a function `height_func()` to convert height in metres to feet.
# The function will ask for a user to input the height.
# You can use: user_input = float(input("Enter your height in metres : ")) to ask user to input height.
# If the input is string data type, the program should print: "Your input is invalid, please try again".
# If a user input is float or integer data type, the program will convert input height to feet 
# and print: "Your height of ___ in metre is ____ in feet." 
# Note that 1 metre = 3.28084 feet.
# The function will loop endlessly, prompting the user to input height until the correct data type is entered.
# The function does not take in any parameters.
# Here is how the program will look like when executed:

    ## Enter your height in metres: two  (user input height as "two")
    ## Your input is invalid, please try again
    ## Enter your height in metres: TWO  (user input height as "TWO")
    ## Your input is invalid, please try again
    ## Enter your height in metres: 2 (user input height as 2)
    ## Your height of 2.0 in metre is 6.56168 in feet.

def height_func():
    pass # pass keyword creates a function without body of code. # Remove pass when inserting body of code.