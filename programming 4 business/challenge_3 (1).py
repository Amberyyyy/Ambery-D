#####  Store your name, email, student_id and class_number as STRINGS #####
ind_assign1 = "challenge 3"
name = "Ambery Teow"
np_email = "S10243481@connect.np.edu.sg"
student_id = "S10243481"
class_number ="WA22" 
employee_info = [['Michael Lee', 8300, 5], ['Ian Wong', 5550, 8],['Michelle Tan', 7500, 11],['Adam Koh', 3050, 2],['Candice Yap', 12000, 12]]


def employment_salary():
    '''
    employment_salary() will return the average salary of the employees
    input should be an integer
    '''
    #creating an empty list to append salary of each worker inside 
    salary=[]
   #for loop to extract the monthly salary for each worker and append to the empty salary list 
    for items in employee_info:
       salary.append(items[1])
    #salary is summed and divided by its length to calculate average salary 
    return f"Average monthly salary per employee :${sum(salary)/len(salary)}"
print(employment_salary())
   






employee_dict = {
    "Michael Lee" : {"Monthly Salary" : 8300, "Years of Employment" : 5},
    "Ian Wong" : {"Monthly Salary" : 5550, "Years of Employment" : 8},
    "Michelle Tan" : {"Monthly Salary" : 7500, "Years of Employment" : 11},
    "Adam Koh" : {"Monthly Salary" : 3050, "Years of Employment" : 2},
    "Candice Yap" : {"Monthly Salary" : 12000, "Years of Employment" : 12}
    }
def employment_dict():
    '''
    employment_dict() will return the average salary of the employees 
    the input should be an integer
     '''
    salary_avg=[]
    for info in employee_dict:
        salary_avg.append(employee_dict[info]["Monthly Salary"])
        
    return f"Average monthly salary per employee:${sum(salary_avg)/len(salary_avg)}"
print(employment_dict())