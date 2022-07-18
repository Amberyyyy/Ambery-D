#####  Store your name, email, student_id and class_number as STRINGS datatype #####
exercise = "functions and loops"
name = "Ambery Teow"
np_email = "S10243481@connect.np.edu.sg"
student_id ="S10243481" 
class_number = "WA22"

###################################################################################
# Q1 
# Write a program that allow users to input temperature and convert temperature 
# from Degrees Celsius to Fahrenheit and vice versa. 
# The program should include 2 functions:

    ##  cel_to_fahren
    # it converts Degrees Celsius to Fahrenheit using celsius * 9/5 + 32
def cel_to_fahren():
    return celcius*9/5+32

celcius=float(input("Enter temperature in Degrees Celsius:"))
fahrenheit = round(cel_to_fahren(),2)
print(f"Temperature in Fahrenheit: {fahrenheit}")


    

    ## fahren_to_cel()
    #  it converts Fahrenheit to Degrees Celsius using (fahrenheit - 32) * 5/9
def fahren_to_cel():
    return (fahrenheit - 32) * 5/9

fahrenheit=float(input("Enter temperature in Fahrenheit: "))
celcius = round(fahren_to_cel(),2)
print(f"Temperature in Celsius: {celcius}")

# Both functions will round decimals to 2 decimal places.

# When `print(cel_to_fahren())` and `print(fahren_to_cel())` is executed, it should display and return:

    ## Enter temperature in Degrees Celsius: 0.55
    ## Temperature in Fahrenheit: 32.99
      
    ## Enter temperature in Fahrenheit: 10.55
    ## Temperature in Celsius: -11.92

# note that 0.55 and 10.55 are user input

###################################################################################
# Q2
# Write a function: deposit_calculator(deposit, interest_rate, no_years).
# The function will accumulate the interest earned per year plus the deposit.

# For example, given a $1000 deposit, 10% interest rate and 5 years, 
# the function will calculate the interest earn in 5 years plus the deposit. 
# When `print(deposit_calculator(1000,0.10,5)` is executed, it should return $1610.51

# Tip to calculate interest earn with deposit: 
# Year 1 = $1100 ($1000 * 1.1)
# Year 2 = $1210 ($1100 * 1.1) 
# Year 3 = $1331 ($1210 * 1.1) 
# Year 4 = $1464 ($1331 * 1.1)
# Year 5 = $1610.51 ($1464 * 1.1)

# Round off decimals to 2 decimal places.

# BONUS: Can you use f-strings to include a $ symbol with the return value?
def  deposit_calculator(deposit, interest_rate,no_year):
  per_year=deposit*interest_rate
  sub_total=per_year+ deposit
  sub_total*=1.1 
  sub_total*=1.1 
  sub_total*=1.1 
  sub_total*=1.1
  for total in range(5,no_year):
    print(total)

  
  
  return round(sub_total,2) 

ans=(deposit_calculator(1000,0.10,5))
print(f"${ans}")
