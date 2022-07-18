#####  Store your name, email, student_id and class_number as STRINGS datatype #####
exercise = "numbers"
name = 'Ambery Teow'
np_email = "S10343481@connect.np.edu.sg"
student_id ="S10243481" 
class_number = "WA22"

##################################################################################
# Write a program to ask user to input two numbers separately.                              
# The program will check if the difference between the 2 numbers is an integer. 
##################################################################################

# The program should display the following when executed:

    ## First execution ##
    # Enter first number : 1.5
    # Enter second number : 0.5
    # 1.5 - 0.5 = 1.0
    # Is the difference between 1.5 and 0.5 an integer? True

    ## Second execution ##
    # Enter first number : 2.5
    # Enter second number : 1.3
    # 2.5 - 1.3 = 1.2
    # Is the difference between 2.5 and 1.3 an integer? False

# Assign `num1` for first number, `num2` for second number 
# Assign `diff` as the difference between `num1` and `num2`  
num_1=(input("Enter first number:"))
num_2=(input("Enter second number:"))
diff=float(num_1)-float(num_2)
print(f"{num_1} - {num_2} = {diff}")
types=float(diff).is_integer()
print(f"Is the difference between {num_1} and {num_2} and integer? {types}")
##################################################################################
# Write a program to ask user to input two numbers separately. 
# The program will use the first number as a base number and second number as an exponent.
# The output should return the value when base number is raised to the exponent. 
##################################################################################

# The program should display the following messages :

    # Enter a base number: 2
    # Enter an exponent: 3
    # 2 to the power of 3 is 8

# Assign `num3` for base number and `num4` for exponent.
# Assign 'raise_power` to store the results of the exponent operation.
num_3=input("Enter a base number:")
num_4=input("Enter an exponent:")
raise_power =int(num_3)**int(num_4)
print(f"{num_3} to the power of {num_4} is {raise_power}")
 