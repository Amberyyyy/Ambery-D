#####  Store your name, email, student_id and class_number as STRINGS #####
ind_assign1 = "challenge 2"
name = "Ambery Teow"
np_email = "S10243481@connect.np.edu.sg"
student_id ="S10243481" 
class_number = "WA22"

def bp(systolic, diastolic):
    #set condtions for the category of Hypertension Crisis
    if systolic>180 or diastolic>120:
        return f"<Systolic {systolic}> <Diastolic {diastolic}> : Hypertension Crisis"
    #set conditions for the category of Hypertension Stage 2
    elif systolic>=140 or diastolic>=90:
        return f"<Systolic {systolic}> <Diastolic {diastolic}> : Hypertension Stage 2"
    #set conditions for the category of Hypertension Stage 1
    elif systolic>=130 or diastolic>=80:
        return f"<Systolic {systolic}> <Diastolic {diastolic}> : Hypertension Stage 1"
    #set condition for the category of elevated 
    elif systolic>=120 and diastolic<80:
        return f"<Systolic {systolic}> <Diastolic {diastolic}> : Elevated"
    #if all of the conditions above are not met , the person falls under the "normal" category 
    else:
        return f"<Systolic {systolic}> <Diastolic {diastolic}> : Normal"
   
#to print output for user to view their blood pressure category and their input 
print(bp(181,100))

    