#####  Store your name, email, student_id and class_number as STRINGS datatype #####
exercise = "conditionals"
name = "Ambery Teow"
np_email = "S10243481@connect.np.edu.sg"
student_id ="S10243481" 
class_number = "WA22"

# Part 1
####################################################################################
# Write a function: income_rebate() to prompt a user to declare his/her monthly income 
# and determine the amount of GST rebate the user should receive.
# It will return the amount of GST rebate based on the following evaluation:

# Monthly Income $ 	                GST rebate $
#------------------                 ------------- 
# 0 to less than 2000 	                1000
# 2000 to less than 5000 	            500
# 5000 to less than 10,000 	            250
# equal or greater than 10,000 	     not eligible

#  Executing `print(income_rebate())` will display and return:

    # Declare your monthly income : 500
    # Your GST rebate is : $1000

    # Declare your monthly income : 4000
    # Your GST rebate is : $500
    
    # Declare your monthly income : 7000
    # Your GST rebate is : $250
    
    # Declare your monthly income : 10000
    # You are not eligible for GST rebate
def income_rebate():
    income=float(input("Declare your monthly income:"))
    if income>=10000:
         return f"You are not eligible for GST rebate"
    elif income >5000:
        return f"Your GST rebate is : $250"
    elif income>2000:
        return f"Your GST rebate is : $500"
    elif income<2000:
        return f"Your GST rebate is : $1000"

print(income_rebate())


   


# Part 2
####################################################################################
# try except else

# Enhance income_rebate() with `try`, `except` and `else` to make it less 
# susceptible to crash. 
# Name the enhanced function as income_rebate_enhanced().
# The enhancement should prevent `ValueError` from crashing the program.
# Tip: Design the function with while loop in mind. The functions will
# keep looping until user input enters a number data type.
# Executing `print(income_rebate())` should display and return the following
# until the user enters a number data type:

    # Declare your monthly income: ten thousand
    # INVALID INPUT (note: put INVALID INPUT in uppercase)

    # Declare your monthly income: one thousand
    # INVALID INPUT (note: put INVALID INPUT in uppercase)

    # Declare your monthly income: 10
    # Your GST rebate is : $1000
def income_rebate_enhance():
    while True:
        try:
            income=float(input("Declare your monthly income:"))
        except ValueError:
            print("INVALID INPUT")
        
        else:
            if income>=10000:
                return f"You are not eligible for GST rebate"
            elif income >5000:
                return f"Your GST rebate is : $250"
            elif income>2000:
                return f"Your GST rebate is : $500"
            elif income<2000:
                return f"Your GST rebate is : $1000"
            break
            
print(income_rebate_enhance())

