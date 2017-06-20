from Database import *

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
    def __init__(self):
        #connect.Inventory_Database()
        #connect.Calendar_Database()
        R = self.Main_search()#Calls on main search function.
        while R != []:#Loops while gear is being selected.
            for line in R:
                print(line)#Results are dsiplayed on console.
            print('Please select a barcode from the list, or hit \'Enter\' to save your current list')
            print('Enter a barcode number')#Message prompting user to select a barcode is on the console.
            item = input('Barcode: ')#User inputs a barcode.
            for line in R:
                if item == '':#User does not enter anything.
                    R = []#Breaks loop.
                    break
                elif item in line:
                    self.Add_Item(line)#Adds item to final list of equipment.
                    R = self.Main_search()#Returns back to function.
                else:
                    None #No acition is taken.
    
    def Main_search(self):
        E = self.Search_field()#Intial search function is called.
        R = self.Reserved()#Function to pull list of reserved gear is called.
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
            else:
                None
        return Item_List#Returns list of gear matching user's input.
    
    def Reserved(self):
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
        ES = Equipment_Search()#Calls equipment search class.
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
