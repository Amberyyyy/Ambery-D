# Create a list named `apparel` with two elements, "shoes" and "shirt".
apparel=["shoes","shirt"]

# Append the string "tie" to apparel using .append().
apparel.append("tie")

# Add the strings "sunnies" and "pants" to apparel using .extend().
extra_apparel=["sunnies","pants"]
apparel.extend(extra_apparel)
# Print the first two items in the apparel list using print() and slice notation.
print(apparel[0:2])
# Print the last item in apparel using print() and index notation.
print(apparel[4])

### Exercise 2 ###
# Create a single string: "running, cycling, swimming" 
# Split the single using .split() method and assign to a variable: sports_list

sports_list = "running, cycling, swimming"
sports_list=sports_list.split(",")

# Verify that sports has three items using len().
print(len(sports_list))

# Create a new list called sports_length using a list comprehension 
sports_length=[]
# that contains the length of each string in sports_list

