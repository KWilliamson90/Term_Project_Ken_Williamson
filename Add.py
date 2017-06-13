from Management import *
from Database import *
from Equipment import *
from Details import *


'''
Postconditon1: Obtains new job number.
Postcondition2: Calls on Job_Details_Window Class.
'''
class Add_Job(Job_Database,EQ_List_Window):#Objective: Create a new job.
    Job_Number = ''#Holds job number

    def __init__(self):
        #connect.Job_Database() (Not in use)
        self.New_num()
        JDW = Job_Details_Window(self.Job_Number)#Gets job details
        JDW.Save_New(Job_Details_Window.Job_Details)#Calls on function to save details
        super().New(self.Job_Number)
        MJW= Main_Job_Window(self.Job_Number)
        

    def New_num(self):#Gets new job number
        num = super().New_Number()
        self.Job_Number = num
