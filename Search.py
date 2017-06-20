from Database import *
from Management import *

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
                MJW = Main_Job_Window()
                MJW.Main(select)#Passes job number to Main Job class.
