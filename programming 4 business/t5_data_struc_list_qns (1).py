#####  Store your name, email, student_id and class_number as STRINGS datatype #####
#from data_str_demoq import weight_age


from distutils.log import info


exercise = "Data Structure"
name = "Ambery Teow"
np_email ="S10243481@connect.np.edu.sg" 
student_id = "S10243481"
class_number ="WA22" 

########################
# Data Structure - LIST
########################

# You are given information of the number of students 
# and school fees of the polytechnics.
# The information is a nested list `polys_info`. 
# The elements in each sub-list contain: 
    ## 1. The institution name
    ## 2. The number of students
    ## 3. Yearly school fee per student

polys_info = [['SP', 4300, 8545], ['NP', 4550, 8650], ['NYP', 4800, 8200], ['RP', 3050, 9050], ['TP', 5200, 8490]]


# 1.
# Write a function `enrollment_summary` with a single parameter `option`. 
# When `1` is supplied to the parameter, `enrollment_summary` will return 
# the total number of students across the polytechnics. 
# When `2` is supplied to the parameter, `enrollment_summary` will return 
# the total school fees revenue collected across the polytechnics. 
# It will return `invalid entry` for any other numbers or strings.

def enrollment_summary(option):
    empty_list=[]
    if option==1:
        for info in polys_info:
            empty_list.append(info[option])
        #return sum(empty_list)
        return (f"Total number of students across the polytechnics:{sum(empty_list)}")
    elif option==2:
        for info in polys_info:
            empty_list.append(info[option]*info[1])
        #return sum(empty_list)
        return(f"Total school fees revenue collected across the polytechnics:${sum(empty_list)}")
    else:
        return "invalid entry"

print(enrollment_summary(2))

# 2.`mean`    
# Write a function `mean` with a single parameter `option`. 
# When `1` is supplied to the parameter, `mean` will return the average number of students 
# across the polytechnics
# When `2` is supplied to the parameter, `mean` will return the average school fees revenue
# collected across the polytechnics. 
# Round the return values to 2 decimal places
polys_info = [['SP', 4300, 8545], ['NP', 4550, 8650], ['NYP', 4800, 8200], ['RP', 3050, 9050], ['TP', 5200, 8490]]
def mean(option):
    empty=[]
    if option==1:
        for data in polys_info:
            empty.append(data[option])
        return f"Average number of students:{round(sum(empty)/len(empty),2)}"
    elif option==2:
        for data in polys_info:
            empty.append(data[1]*data[option])
        return f"Average school fees revenue:: {round(sum(empty)/len(empty),2)}"

print(mean(option=2))       
            

        
# 3.`median`
# Write a function `median` with a single parameter `option`. 
# When `1` is supplied to the parameter, `median` will return the 
# median number of students of the polytechnics
# When `2` is supplied to the parameter, `median` will return the 
# median yearly school fees of the polytechnics. 

polys_info = [['SP', 4300, 8545], ['NP', 4550, 8650], ['NYP', 4800, 8200], ['RP', 3050, 9050], ['TP', 5200, 8490]]
def median(option):
    empty_list=[]
    if option==1:
        for items in polys_info:
            empty_list.append(items[option])
            empty_list.sort()
            index=int(len(empty_list)/2)
        return f"Median number of students:{empty_list [index]}"
    if option==2:
        for items in polys_info:
            empty_list.append(items[option])
            empty_list.sort()
            index=int(len(empty_list)/2)
        return f"Median yearly school fees:${empty_list[index]}"
print(median(option=2))

# Executing the functions will display and return:

    ## print(enrollment_summary(1))
    ## Total number of students across the polytechnics: 21900

    ## print(enrollment_summary(2))
    ## Total school fees revenue collected across the polytechnics: $187211500

    ## print(mean(1))
    ## Average number of students: 4380.0

    ## print(mean(2))
    ## Average school fees revenue: $37442300.0

    ## print(median(1))
    ## Median number of students: 4550

    ## print(median(2))
    ## Median yearly school fees: $8545