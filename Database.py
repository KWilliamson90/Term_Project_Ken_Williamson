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
                self.Jobs.remove(line)
            else:
                None#No action is taken.
