from multiprocessing import Queue
'''
Postcondition1: Hold details for every job in a database.
Postcondition2: Generate new job number based on previous job number.
'''
class Job_Database():#Objective: All actions that require Job.db
    Jobs = Queue()#Holds jobs in queue until database is built.
    
    def Add_New(self,Job_Details):
        self.Jobs.put(Job_Details)#Adds job details to Queue
        print(Job_Details)#Job Details is on the console.

    def New_Number(self):
        Number = 1#Default number
        '''try:
            Last_Job = self.Jobs.get()
            Number = Last_Job['Job Number']
            int(Number) + 1
        except:
            Number = 1'''#Ideally the code you be something like this.
        return Number #Returns new job number.

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
        super().Add_New(Job_Details)#Job details are added to database.

    def __init__(self,Job_Number):
        self.Entry_Fields(Job_Number)#Calls on function to obtain details
        self.Save_New(self.Job_Details)#Calls on function to save details

'''
Postconditon1: Obtains new job number.
Postcondition2: Calls on Job_Details_Window Class.
'''
class Add_Job(Job_Database):#Objective: Create a new job.
    Job_Number = ''#Holds job number

    def __init__(self):
        #connect.Job_Database() (Not in use)
        self.New_num()
        JDW = Job_Details_Window(self.Job_Number)#Gets job details
        #Save_New.Job_Details_Window() (Not is use)
        #New.EQ_List_Window(num) (Not in use)

    def New_num(self):#Gets new job number
        num = super().New_Number()
        self.Job_Number = num
        

print('Welcome to \"Rental X\": The best rental software.')
print('Please Enter a command.')
print('\n \"Add Job\"')
Command = input('Enter: ')

if Command == 'Add Job':
    AJ = Add_Job()
else:
    print('Try Again')
