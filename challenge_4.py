#####  Store your name, email, student_id and class_number as STRINGS #####
ind_assign1 = "challenge 4"
name = "Ambery Teow"
np_email = "S10243481@connect.np.edu.sg"
student_id = "S10243481"
class_number ="WA22" 

def fitness_app(distance):
    '''
    fitness-app helps calculate the points earned from the distance the user ran
    input should be an integer 
    '''
    #setting up culculation of points for distance more than 48km
    if distance>48:
        return (distance-48)*600+8*550+8*325
    #setting up calculations of points for distance more than 40km
    elif distance>=41:
        return (distance-40)*550+8*325
    #setting up calculations if points for distance more than 32km
    elif distance>=33:
        return (distance-32)*325
    #if the distance ran by user do not meet any of the requirements above ,user must have ran less than 32km
    #hence the points earned would be 0 for any value below 32 
    else:
        return 0
    
print(fitness_app(50))
