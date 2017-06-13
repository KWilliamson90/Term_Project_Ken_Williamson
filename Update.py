from Database import *
from Details import *

'''
Precondition1: Given details of select job.
Postcondition1: Opens Job Details Window class.
Postcondition2: Calls on Update function database and passes new details to said function.
'''        

class Update_Job(Job_Database):#Objective: Update select job.
    def __init__(self,Job):
        Job_Details_Window.Job_Details = Job #Passes details of currect job to Job Details Window class.
        JDW = Job_Details_Window(Job['Job Number'])#Calls on Job Details Window class and provides job number.
        super().Update_Job(Job_Details_Window.Job_Details)#Passes changes made to Job Database class for updating.
