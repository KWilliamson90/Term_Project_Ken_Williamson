from Database import *

'''
Postcondition1: Create a dictionary with all the details of the job.
Postcondition2: Add job details to database.
'''
class Job_Details_Window(Job_Database):#Objective: Allow user to enter job details
    Job_Details = {}#Holds job details

    def Entry_Fields(self,Job_Number):
        Client = input('Enter Client Name: ')#User enters client name
        Address = input('Enter Address: ')#User enters Address
        Contact = input('Enter Contact Info: ')#User enters contact info
        Start = input('Enter Start Date: ')#User enters start date.
        End = input('Enter End Date: ')#User enters end date.
        self.Job_Details['Job Number'] = Job_Number
        self.Job_Details['Client'] = Client
        self.Job_Details['Address'] = Address
        self.Job_Details['Contact'] = Contact
        self.Job_Details['Start'] = Start
        self.Job_Details['End'] = End

    def Save_New(self,Job_Details):
        super().Add_New_Job(Job_Details)#Job details are added to database.

    def __init__(self,Job_Number):
        self.Entry_Fields(Job_Number)#Calls on function to obtain details
