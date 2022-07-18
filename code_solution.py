#####  Store your name, email, student_id and class_number as STRINGS datatype #####
exercise = "individual assignment 2"
name ="Ambery Teow"
np_email ="S10243481@connect.np.edu.sg"
student_id ="S10243481"
class_number ="TA22"

# The following modules are imported to kickstart your assignment:
from pathlib import Path
import re, csv

### Tips for the assignment ###

# 1. Set file paths to pfb_ind_assign2 folder for reading and writing files.
# 2. Create search pattern for rental, address, flat type and date
# 3. Iterate over tenancy documents 
     # For each file open as read mode:
          ## 3.1 search and return rental, address flat type and dates
          ## 3.2 clean up the extracted data 
          ## 3.3 for each matched item, append to tenancy.csv
fp=Path.cwd()
#creaet tenancy file to append all the data 
file_path=Path.cwd()/"tenancy.csv"
file_path.touch()

# create headings to append
headings=["ADDRESS","FLAT","START DATE","END DATE","RENTAL"]
# write the heading in the tenancy csv file 
with file_path.open(mode="a",encoding="UTF-8",newline="")as file:
        # create writer object 
        writer=csv.writer(file)
        #write heading 
        writer.writerow(headings)
#create fro loop to excess all the test documents 
for file in fp.glob("*.txt"):
        #read the text documents 
        with file.open(mode="r",encoding="UTF-8")as data:
                items = data.read()
                #extract the data using regex
                address=re.findall(pattern="Block [0-9]+ Unit.+[0-9][0-9][0-9][0-9][0-9][0-9]",string=items)
                flat_type=re.findall(pattern="[0-9] ROOM FLAT",string=items)
                date=re.findall(pattern="[0-9]+-[0-9]+-[0-9]+",string=items)
                rental=re.findall(pattern="[A-Z][A-Z][A-Z][0-9]+",string=items)
          #open csv file      
        with file_path.open(mode="a",encoding="UTF-8",newline="")as file:
                #create writer object so that we can write strings into the csv file
                writer=csv.writer(file)
                #arrange everything in order into a list 
                all_data=(address+flat_type+date+rental)
                #write everything into the csv file 
                writer.writerow(all_data)


