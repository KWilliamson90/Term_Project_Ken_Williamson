from multiprocessing import Queue
from Database import *
from Management import *
from Equipment import *
from Search import *


'''
Postcondition1: Greet the user with a message.
Postcondition2: Prompt user to choose an action.
Postcondition3: Call on proper class depending on User's command.
'''
        
class Main_Menu():
    def __init__(self):
        print('Welcome to \"Rental X\": The best rental software.')#Welcome message is on the console.
        print('Please Enter a command.')#Prompts user to enter a command.
        print('\n \"Add Job\"')#Add Job option.
        print('\n \"Search Job\"')#Search Job Option
        Command = input('Enter: ')#User inputs command.
        MJW = Main_Job_Window()

        if Command == 'Add Job':#User inputs 'Add Job'
            MJW.Add_Job()#Calls on Add Job class
        elif Command == 'Search Job':#User inputs 'Search Job'
            SJ = Job_Search()#Calls on Search Job class.
        else:
           print('Try Again')#User's input is incorrect.

Main_Menu()
