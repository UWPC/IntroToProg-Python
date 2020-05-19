# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# PCoonrad,5.15.2020, Added code > Processing - Step 1
# PCoonrad,5.15.2020, Added code > Input/Output - Steps 2,3
# PCoonrad,5.16.2020, Added code > Input/Output - Steps 4
# PCoonrad,5.17.2020, Added code > Input/Output - Step 5
# PCoonrad,5.18.2020, Added code > Input/Output - Step 6,7
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None
strFile = "ToDoList.txt"  # An object that represents a file
dicRow = {"Task": 0, "Priority": 1}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # Capture the user option selection
strTask = ""  # Tasks
strPriority = ""  # Priorities

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
print("Load data from 'ToDoList.txt' file:")
objFile = open(strFile, "r")
for row in objFile:
    lstRow = row.split(",")  # Returns a list!
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
#    print(dicRow)
print(lstTable)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
Please choose from below Menu of Options:    

    Menu of Options:
       1) Show current data.
       2) Add a new item.
       3) Remove an existing item.
       4) Save Data to File.
       5) Exit Program.
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
    # TODO: Add Code Here
        print("\nYour Current ToDo List is: ")
        print("\nTASK", "\t\t", "PRIORITY")
        for row in lstTable:
            print(row["Task"], "\t", row["Priority"])
        continue

    #Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
         # TODO: Add Code Here
        while (True):
            strNewTask = input("Enter a New Task: ")
            strNewPriority = input("Enter a New Priority: ")
            lstTable.append({"Task": strNewTask.capitalize(), "Priority": strNewPriority})
            #print(lstTable)  # test code: verify task is added
            strChoice = input("Exit? ('Y/N'): ")
            if strChoice.lower() == "y": break
            else:
                continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        while(True):
            strRmTask = input("Enter Task to Remove: ")
            for row in lstTable:
                if row["Task"].lower() == strRmTask.lower():
                    lstTable.remove(row)
                    print("Row was removed.")
                    #print(lstTable)  # test code: verify task is removed
                    break
            else:
                print("Row not found.")
                # print(lstTable)  # test code: verify row not found
            strChoice = input("Exit? ('Y/N'): ")
            if strChoice.lower() == "y": break
            continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(str(row["Task"]) + ',' + str(row["Priority"] + "\n"))
        objFile.close()
        print("Data was saved!")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        strChoice = input("Would you like to 'Exit and Close' the program? ('Y/N'): ")
        if strChoice.lower() == "y":
            print("\nThank You!")
            break
        else:
            continue


