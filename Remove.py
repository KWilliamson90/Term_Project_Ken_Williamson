from Database import *


'''
Precondition1:Given the details of current job.
Postcondition1: Message asking user if they are certain they wish to remove select job is on the console.
Postcondition2: User selects 'Yes' job is removal function is called, OR return to Main Job Window.
'''

class Remove_Job(Job_Database):#Objective: Removes select job from Job Database.
    def __init__(self,Details):
        command = input('Are you sure you want to remove this job?: ')#Prompts user to be certain they wish to remove job.
        if command == 'Yes':#User wants to remove job.
            super().Remove_Job(Details)#Calls on function to remove job from database.
        else:#User does not wish to remove job.
            None
