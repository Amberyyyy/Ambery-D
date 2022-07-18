######## Example of single value variables ########
# 1. Weight data (in kg) for each individual
andy_weight = 68
candy_weight = 55
mandy_weight = 65
randy_weight = 45

# 2. age data (in years) for each individual
andy_age = 49
candy_age = 40
mandy_age = 30
randy_age = 25

######## Example of weight data packed as a tuple and a list ########
weight_tuple = (68, 55, 65, 45)  #parenthesis()--tuple
weight_list = [68, 55, 65, 45] #square bracket[] --list is more useful
# differencein list and tuple is the way the bracket is being used 

######## Example of age data packed as a tuple and a list ########
age_tuple = (49,40,30,25) #typle
age_list = [49,40,30,25] #list 

######### Example of weight data packed as a dictionary ########
# Dictionary allow use to relate the person's name to his/her weight.
# key and value pair # use curly braces 
#key - person name #value--weight
# key usually contain a quotation mark
weight_dict = {
    "andy" : 68, 
    "candy" : 55,
    "mandy" : 65,
    "randy" : 45
    }

######### Packing age and weight paced into a nested dictionary ########
# Dictionary stored data in a more compact way.
# a dictionary within a another dictionary 
weight_age_dict = {
    "andy" : {"weight":68, "age": 49},# another dictionary within a dictionary 
    "candy" : {"weight":55, "age": 40},
    "mandy" : {"weight":65, "age": 30},
    "randy" : {"weight":45, "age": 25},
    }
# dictionary is usually not written in a single line as it would be easier to read and easier to spot mistakes like mssing colon/comma etc

######### Explore methods in a list #########
# Tuple has very little methods since it is immutable.
age_list = [49,40,30,25]
age_list.sort()#arrange from smallest to the largest 
age_list.append(500)# add a value to the list at the end 
print(age_list)


#########  Iteration and slicing on a list #########
# same iteration for tuple
#age_list = [49,40,30,25]
#indexing and slicing ---using index position of list and slice them 
#print(age_list[0]) #iterable ---use a while or for loop to perform action on them 
#print(age_list[1])
#print(age_list[2])
#print(age_list[0:3])
#for age in age_list:
 #   print(age+10)# add 10 to all the ages in the list using a loop



######### Let's put data of each person into a nested list #########
# In the order of name, weight and age in each sublist.
data = [["andy", 68, 49 ], ["candy", 55, 40], ["mandy", 65, 30], ["randy", 45, 25]]
#lsit allow different types of data to be packed together
print(len(data))
print(len(data[0]))
#data[0]--- output = ["andy",68,49]
#data[0][0]#output :andy 
#########  Iterate over the nested list ######### 
for people in data:
    print(people)
    print(people[0])

#########  Find the average weight in the nested list ######### 
empty=[]
data = [["andy", 68, 49 ], ["candy", 55, 40], ["mandy", 65, 30], ["randy", 45, 25]]
for people in data:
    empty.append(people[1])# can change the index in the [] to exrtact what you want (name/age/weight)
print(sum(empty)/len(empty))# adding everythign together and then divide
# dont print(sum(empty)/4----this is hard coding , only work in one way 




# finding average age 
empty1=[]
for people in data:
    empty1.append(people[2])
print(sum(empty1)/len(empty1))



######### Set up a function to find average weight and age with a parameter: option #########
# Parameter accepts value 1 or 2, where 1 is the index for weight and 2 is the index for age.

data = [["andy", 68, 49 ], ["candy", 55, 40], ["mandy", 65, 30], ["randy", 45, 25]]
def weight_age(option):
    empty_list=[]
    if option==1:
        for people in data:
            empty_list.append(people[option])
        return sum(empty_list)/len(empty_list)
    elif option==2:
        for people in data:
            empty_list.append(people[option])
        return sum(empty_list)/len(empty_list)
    elif option==3:
        for people in data:
            empty_list.append(people[1]*people[2])#multiply age and weight together and put in empty list 
        return sum(empty_list)#add everything in the empty list 
    else: 
        return"invalid"
print(weight_age(option=3))
    #return empty_list( if you are confused try me only and comment out the code above)


######### Finding median (middle value) #########
# For even numbers of elements, sum the 2 elements in the middle and divide by 2
weight_even = [68, 55, 65, 45]

# divide length by 2 to find index of 2nd element in the middle
# convert float to integer for indexing purpose


# minus 1 to find index of 1st element in the middle


# sum the 2 elements in the middle and divide by 2


# For odd numbers in elements, simply divide by 2
weight_odd = [68, 55, 65, 45, 80]
# convert float to integer for indexing purpose
# int() will also truncate the decimal place.


