#####  Store your name, email, student_id and class_number as STRINGS #####
ind_assign1 = "challenge 1"
name = "Ambery Teow"
np_email = "S10243481@connect.np.edu.sg"
student_id ="S10243481" 
class_number = "WA22"

def valid_pin(pin):
    #setting conditions for when the pin have 8 characters to return true
   if len(pin)==8:
       return True
    #setting the conditions for when the pin have 14 characters to return true
   elif len(pin)==14:
       return True
    #when the pin does not meet the conditions of having 8 or 14 characters , return False 
   else:
       return False
print(valid_pin("9876"))

    