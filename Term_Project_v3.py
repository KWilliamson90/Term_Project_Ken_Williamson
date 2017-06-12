from multiprocessing import Queue

'''
Precondition1: Holds every Equipment List created.
Postcondition1: Provides connection to Database.
Postcondition2: Adds new equipment list to Database.
'''
class Equipment_Database():#Objective: Provides all functions needed to make changes to Equipment Database.
    Equipment_List_Master = Queue()#Holds all list of Equipment.

    def connect(self):#Connects to Database.
        None #Disabled until database is built.
    def Add_New_EQ(self,EQ):#Adds to Equipment list to Database.
        self.Equipment_List_Master.put(EQ)#Places equipment into Queue instead of Database for now.

'''
Precondition1: Holds a running list of every equipment that is reserved and when.
Postcondition1: Provides connection to Database.
Postcondition2: Adds list of equipment into the respective columns for the days they are reserved on.
'''

class Calendar_Database():#Objective: Provides all functions needed to make changes to Calendar Database.
    Reserved_Equipment = [{'Job':'0002','Barcode':'1002'}]#List of every item that is currecntly reserved in place of a Database.
    def connect(self):#Connects to Database.
        None #Disabled until database is built.
    def Add_New_Cal(self,EQ): #Adds equipment to reserved list.
        for line in EQ:
            self.Reserved_Equipment.append(line)#Adds equipment line by line instead of adding a list within a list.

class Inventory_Database():#Objective: Provides all functions needed to make changes to Inventory Database.
    Inventory = [{'Barcode':'1000','Type':'Video','Subtype':'Camera','Name':'Canon EOS C300 Digital Cinema Camera','Purchase Order':'PO 346','Purchase Price':'8,000','Job':'','Location':'','History':''},{'Barcode':'1002','Type':'Video','Subtype':'Camera','Name':'Canon EOS C300 Digital Cinema Camera','Purchase Order':'PO 346','Purchase Price':'8,000','Job':'','Location':'','History':''},{'Barcode':'1001','Type':'Audio','Subtype':'Recorder','Name':'Sound Devices 664 Digital Field Recorder','Purchase Order':'PO 657','Purchase Price':'2,000','Job':'','Location':'','History':'',}]
    def connect(self): #Connects to Database.
        None #Disabled until database is built.

    def Update_Job(self,Job_Number,EQ):#Updates details of every item that is reserved on current list.
        for line in self.Inventory:#Search through database.
            for item in EQ:#Runs through list of equipment to be reserved.
                for key in item.keys():#Idenifies the barcodes in the list.
                    if key == line['Barcode']:#Barcodes on given equipment list matches the barcodes in Inventory Database.
                        line['Job'] = Job_Number#The item details now reflect that the item is going on select job.
                    else:
                        None #If barcodes do not match, no action is taken.

    def Update_History(self,Job_Number,EQ):#This function should move job number that was previously in the 'Job' field of the items details into this field.(Currently repeats 'Update_Job' function.) 
        for line in self.Inventory:
            for item in EQ:
                for key in item.keys():
                    if key == line['Barcode']:
                        line['History'] = Job_Number
                    else:
                        None
            

'''
Precondition1: Hold details for every job in a database.
Postcondition1: Generate new job number based on previous job number.
Postcondition2: Connects to Database.
Postcondition3: Creates new row in database for new job.
Postcondition4: Updates details of a job in database.
Postcondition5: Removes job from database.
'''
class Job_Database():#Objective: Provides all functions needed to make changes to Job Database.
    Jobs = []#Holds jobs in list until database is built.

    def connect(self):#Provides connection to database.
        Old_Jobs = [{'Job Number':2,'Client':'John Smith','Address':'42 Circle Drive','Contact':'555-555-5555','Start':'2/1/2018','End':'2/2/2018'},{'Job Number':3,'Client':'Dan Wilson','Address':'20 Fairfield Ave','Contact':'555-555-5555','Start':'2/3/2018','End':'2/22/2018'},{'Job Number':4,'Client':'Mark Jackson','Address':'24 Short St','Contact':'555-555-5555','Start':'3/1/2018','End':'4/1/2018'},{'Job Number':5,'Client':'William Rook','Address':'66 School St','Contact':'555-555-5555','Start':'3/2/2018','End':'3/5/2018'}]
        for job in Old_Jobs: #Runs through item in list.
            self.Jobs.append(job)#Adds jobs to main list of jobs.
    
    def Add_New_Job(self,Job_Details):
        self.Jobs.append(Job_Details)#Adds job details to main list.

    def New_Number(self):#Generates new job number
        Number = 1#Default number
        '''try:
            Last_Job = self.Jobs.get()
            Number = Last_Job['Job Number']
            int(Number) + 1
        except:
            Number = 1'''#Ideally the code you be something like this.
        return Number #Returns new job number.

    def Update_Job(self,Details):#Updates details of a job in the database
        for line in self.Jobs:#Runs through every job in main list.
            if line['Job Number'] == Details['Job Number']:#Identifies correct job by Job Number.
                line = Details #Replaces job details with new details.

    def Remove_Job(self,Details):#Removes Job from database.
        for line in self.Jobs:#Runs through every job in main list.
            if line['Job Number'] == Details['Job Number']:#Identifies correct job by Job Number.
                self.Jobs.remove(line)#Removes job from main list
                SJ = Job_Search()#Returns to Job Search class instead of Main Menu for now.
            else:
                None#No action is taken.

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
            MJW = Main_Job_Window()#Return to Main Job Window.
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
        elif command == 'Remove Job':#User chooses to Remove Job.
            RJ = Remove_Job(self.Main_Job)#Calls on function to Remove Job.
        else:
            print('Try Again')#User enter's incorrectly.

'''
Precondition1: Given a start date and end date.
Postcondition1: Connects to Inventory Database
Postcondition2: Connects to Calendar Database.
Postcondition3: Prompts user to enter a item name.
Postcondition4: Creates list of gear with matching names from Inventory Database.
Postcondition5: Creates of reserved gear based on given start and end dates from Calendar Database.
Postcondition6: Removes reserved gear from list of matching name items from Inventory Database.
Postcondition7: Displays final list of available gear.
Postcondition8: Prompts user to select a barcode from available gear list.
Postcondition9: Adds select item to final list of equipment, unless item has already been added.
Postcondition10: Returns final list of select gear.
'''

class Equipment_Search(Inventory_Database,Calendar_Database):#Objective: Act as search engine of available equipment.
    Equipment = []#Final list of equippment.
    def __init__(self,Start,End):
        #connect.Inventory_Database()
        #connect.Calendar_Database()
        R = self.Main_search(Start,End)#Calls on main search function.
        while R != []:#Loops while gear is being selected.
            for line in R:
                print(line)#Results are dsiplayed on console.
            print('Enter a barcode number')#Message prompting user to select a barcode is on the console.
            item = input('Barcode: ')#User inputs a barcode.
            for line in R:
                if item == '':#User does not enter anything.
                    R = []#Breaks loop.
                elif item in line:
                    self.Add_Item(line)#Adds item to final list of equipment.
                    R = self.Main_search(Start,End)#Returns back to function.
                else:
                    None #No acition is taken.
    
    def Main_search(self,Start,End):
        E = self.Search_field()#Intial search function is called.
        R = self.Reserved(Start,End)#Function to pull list of reserved gear is called.
        F = self.Final_result(E,R)#Function to create final list of avaiable gear to book.
        return F #Returns list of potential gear to reserve for job.

    def Final_result(self,E,R):
        final_list = []#Holds list of available gear.
        for item in E:#Runs through list of gear that matchs user's input.
            for line in R:#Runs through list of already reserved equipment.
                if item['Barcode'] == line['Barcode']: #Identifies items that are on both lists.
                    None#No action is taken.
                else:#Items that are not reserved are identified.
                    L = {item['Barcode']:item['Name']}#Creates a display friendly dictionary.
                    final_list.append(L)#Adds variable to available gear list.
        return final_list#Returns list of available gear.
    
    def Search_field(self):
        Item_List = []#Holds items that fit description.
        Field = input('\nEnter Item Name: ')#Prompts User to enter a item name.
        for line in Inventory_Database.Inventory:#Runs through Inventory Database.
            item = line['Name']#Identifies Item's name.
            item = item.lower()#Makes item lowercase.
            if Field in item:#Identifies Items with names matching the User's Input.
                Item_List.append(line)#Adds Item to list.
        return Item_List#Returns list of gear matching user's input.
    
    def Reserved(self,Start,End):
        #Create a list of gear that is already booked based on given dates.
        Reserved_list = []#List of gear that is already reserved between given dates.
        for line in Calendar_Database.Reserved_Equipment:#Runs through Calendar database based on given dates.
            Reserved_list.append(line)#Adds every item reserved to list.
        return Reserved_list#Returns list of reserved gear.

    def Add_Item(self,line):
        if line in self.Equipment:#Identifies gear already on the list.
            print('Already Booked')#Alerts user that item is already reserved.
        else:
            self.Equipment.append(line)#Adds item to list of final equipment.

'''
Precondition1: Given list of equipment.
Postconditon1: Create new equipment list.
Postcondition2: Display list of equipment.
Postcondition3: Prompt user to save equipment list.
Postcondition4: Save changes to all database.
Postcondition5: Closes connections with all Databases except for Job database.
'''

class EQ_List_Window(Equipment_Search,Inventory_Database,Calendar_Database, Equipment_Database):#Objective: Display list of equipment and hold functions that makes changes to equipment list and database.
    Equipment_List = []#Holds list of equipment.
    Start = '' #Start date
    End = '' #End Date
    def New(self,Job_Number):#Called when new equipment list is created.
        #connect.Equipment_Database()
        #Get_Dates(num)
        ES = Equipment_Search(self.Start,self.End)#Calls equipment search class.
        self.Display()#Calls on function to display equipment list on console.
        self.Save_New(Job_Number)#Calls on function to save equipment list.
    
    def Display(self):
        print('\n')#Space.
        for Line in Equipment_Search.Equipment:#Runs through equipment list given from Equipment Search class.
                print(Line)#Displays item on console.
        cmd = input('Press Enter to Save list')#Prompts user to hit 'Enter' to save list.
        self.Equipment_List = Equipment_Search.Equipment #Saves equipment list from Equipment Search class as main equipment list.
        
    
    def Save_New(self,Job_Number):
        EQ = self.Equipment_List#Variable for equipment list.
        super().Add_New_Cal(EQ)#Calls on function to add equipment to Calendar Database.
        super().Update_Job(Job_Number,EQ)#Calls on function to add job number to every item's details.
        super().Update_History(Job_Number,EQ)#Calls on function to add job number to every item's details.
        #super().Add_New(EQ)
        #self.Close()

    def Close(self):
        None#No action is taken currently.
        #closeConnect.Inventory_Database()
        #closeConnect.Equipment_Database()
        #closeConnect.Calendar()
    

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
        

print('Welcome to \"Rental X\": The best rental software.')#Welcome message is on the console.
print('Please Enter a command.')#Prompts user to enter a command.
print('\n \"Add Job\"')#Add Job option.
print('\n \"Search Job\"')#Search Job Option
Command = input('Enter: ')#User inputs command.


if Command == 'Add Job':#User inputs 'Add Job'
    AJ = Add_Job()#Calls on Add Job class
elif Command == 'Search Job':#User inputs 'Search Job'
    SJ = Job_Search()#Calls on Search Job class.
else:
   print('Try Again')#User's input is incorrect.
