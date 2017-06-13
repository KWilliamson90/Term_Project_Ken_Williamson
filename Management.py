from Database import *
from Update import *
from Remove import *

'''
Precondition1: Given job number to display on console.
Postcondition1: Search through job database for job details based on job number.
Postcondition2: Displays every detail about select job on console.
Postcondition3: Displays options for what the user can do next.
Postcondition4: Prompts user to enter a select option.
Postcondition5: Calls on function based on User's input.
'''

class Main_Job_Window(Job_Database):#Objective: Display job details and additional commands.
    Main_Job = {}#Holds details of current job.
    def __init__(self,Job_Number):
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
        print('\n\"Add Equipment\" (Unavailable at this time)')#Disabled option.
        print('\n\"Update Job\"')#Option to Update Job.
        print('\n\"Remove Job\"')#Option to Remove Job

        command = input('Enter: ')#Prompts User to enter a option.
        if command == 'Update Job':#User chooses to Update Job.
            UJ = Update_Job(self.Main_Job)#Calls on function to Update Job.
            self.Display()
        elif command == 'Remove Job':#User chooses to Remove Job.
            RJ = Remove_Job(self.Main_Job)#Calls on function to Remove Job.
        else:
            print('Try Again')#User enter's incorrectly.

'''
Postcondition1: Connects to Job Database.
Postcondition2: Prompts user to enter a job number.
Postcondition3: Displays list of potential jobs for the user to select.
Postcondition4: Prompts user to select correct job.
Postcondition5: Passes job number to Main Job Window class.
'''

class Job_Search(Job_Database):#Objective: Act as search engine to find jobs in Job Database.
    def __init__(self):
        selection = []#Holds potential jobs for user to select.
        super().connect()#Connects to Job Database.
        field = int(input('Enter a Job Number: '))#Prompts User to enter a job number.
        for job in Job_Database.Jobs:#Runs though Job Database.
            if field == job['Job Number']:#Identifies potential jobs.
                print(str(job['Job Number']) +': ' + job['Client'])#Displays job number and client name on console. 
                selection.append(job)#Adds potentails jobs to list.
            else:
                None#No action is taken on jobs that do not match.
        select = int(input('\nEnter a job number from the list above: '))#Prompts User to select correct job.
        for line in selection:#Runs through potential job list.
            if select == line['Job Number']:#Identifies correct job.
                MJW = Main_Job_Window(select)#Passes job number to Main Job class.
