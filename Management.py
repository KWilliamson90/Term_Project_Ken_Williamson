from Database import *
from Equipment import *
from Details import *

'''
Precondition1: Given job number to display on console.
Postcondition1: Search through job database for job details based on job number.
Postcondition2: Displays every detail about select job on console.
Postcondition3: Displays options for what the user can do next.
Postcondition4: Prompts user to enter a select option.
Postcondition5: Calls on function based on User's input.
'''

class Main_Job_Window(Job_Database):#Objective: Display job details and additional commands.
    Job_Number = ''#Holds job number
    Main_Job = {}#Holds details of current job.
    def Main(self,Job_Number):
        for eqlist in Job_Database.Jobs:#Runs through Job Database.
            if Job_Number == eqlist['Job Number']:#Identifies correct job based on given job number.
                self.Main_Job = eqlist #Adds job details to variable.
            else:
                None#No action is taken.
        self.Display()#Calls on funtion to display job details.

    def Display(self):
        print('\n')
        print('Job Number: ' + str(self.Main_Job['Job Number']))#Job Number is on console
        print('Client: ' + self.Main_Job['Client'])#Client name is on console.
        print('Address: ' + self.Main_Job['Address'])#Adress is on console.
        print('Contact: ' + self.Main_Job['Contact'])#Contact is on console.
        print('Start Date: ' + self.Main_Job['Start'])#Start Date is on console.
        print('End Date: ' + self.Main_Job['End'])#End Date is on console.
        print('\n')
        print('Please Select an option')#Message to prompt user to select an option is on the console.
        print('\n\"Add Equipment List\"')#Disabled option.
        print('\n\"Update Job\"')#Option to Update Job.
        print('\n\"Remove Job\"')#Option to Remove Job

        command = input('Enter: ')#Prompts User to enter a option.
        if command == 'Update Job':#User chooses to Update Job.
            self.Update_Job(self.Main_Job)#Calls on function to Update Job.
            self.Display()
        elif command == 'Remove Job':#User chooses to Remove Job.
            self.Remove_Job(self.Main_Job)#Calls on function to Remove Job.
        elif command == 'Add Equipment List':
            num = self.Main_Job['Job Number']
            self.Add_EQ(num)
            self.Display()
        else:
            print('Try Again')#User enter's incorrectly.

    def Add_Job(self):
        #connect.Job_Database() (Not in use)
        self.New_num()
        JDW = Job_Details_Window(self.Job_Number)#Gets job details
        JDW.Save_New(Job_Details_Window.Job_Details)#Calls on function to save details
        self.Add_EQ(self.Job_Number)
        self.Main(self.Job_Number)

    def New_num(self):#Gets new job number
        num = super().New_Number()
        self.Job_Number = num

    def Add_EQ(self,Job):
        EQ = EQ_List_Window()
        EQ.New(Job)

    def Update_Job(self,Job):
        Job_Details_Window.Job_Details = Job #Passes details of currect job to Job Details Window class.
        JDW = Job_Details_Window(Job['Job Number'])#Calls on Job Details Window class and provides job number.
        super().Update_Job(Job_Details_Window.Job_Details)#Passes changes made to Job Database class for updating.

    def Remove_Job(self,Job):
        command = input('Are you sure you want to remove this job?: ')#Prompts user to be certain they wish to remove job.
        if command == 'Yes':#User wants to remove job.
            super().Remove_Job(self.Main_Job)#Calls on function to remove job from database.
        else:#User does not wish to remove job.
            None
