# ----------------------------------------------------------------------------------- #
# Title: HR System
# Description: Keeps track of employee information. PLANNED USAGE FOR A FRIEND!!!
#              NOT A PROGRAMMER!!!
# ChangeLog (Jack Kennedy,04/26/2020,Reread to not overcomplicate things):
# JJack,4.26.2021,Created started script
# Jack Kennedy, 04/26/2021, Worked on script
# ----------------------------------------------------------------------------------- #
# GOALS
# Set Up Data Structure = CHECK
# Organize Data Structure by ID/Social (It's on the data, it's not secret) = CHECK
# Create reminder to make reviews with employees 3 months past prior review = NOT DONE
#               Set date to

# Imports
import csv
import datetime

# Data

masterList = []
dicRow = {}
# Primary data stored here
wholeActive = []
wholeNot_active = []
txtData = []


# Processing
class Processor:
    # Reads the CSV file and captures it into "masterList", a list that stores dictionaries
    @staticmethod
    def read_data_from_file_master_list():
        global masterList
        global dicRow
        with open('employees.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print("Loading in Employees.csv File...")
                line_count += 1
                dicRow = {"Name": row["Name"], "Address": row["Address"], "Social": row["Social"],
                          "Date of Birth": row["Date of Birth"], "Job Title": row["Job Title"],
                          "Start Date": row["Start Date"], "End Date": row["End Date"]}
                masterList.append(dicRow)
                line_count += 1

    @staticmethod
    def update_file():
        global masterList
        global dicRow
        masterList = []
        with open('employees.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print("Loading in Employees.csv File...")
                line_count += 1
                dicRow = {"Name": row["Name"], "Address": row["Address"], "Social": row["Social"],
                          "Date of Birth": row["Date of Birth"], "Job Title": row["Job Title"],
                          "Start Date": row["Start Date"], "End Date": row["End Date"]}
                masterList.append(dicRow)
                line_count += 1

    # Resets itself then uses the Master List to sort though the data. Means only Master list used
    @staticmethod
    def sort_data():
        global wholeActive
        global wholeNot_active
        wholeActive = []
        wholeNot_active = []
        count = 0
        try:
            while count <= len(masterList):
                if masterList[count].get("End Date") == "Active":
                    wholeActive.append(masterList[count])
                    count += 1
                if masterList[count].get("End Date") != "Active":
                    wholeNot_active.append(masterList[count])
                    count += 1
        except IndexError:
            pass

    @staticmethod
    def data_sorter_by_ssn(first, second, third):
        global masterList
        global wholeActive
        global wholeNot_active
        first = sorted(first, key=lambda i: i["Social"])
        second = sorted(second, key=lambda i: i["Social"])
        third = sorted(third, key=lambda i: i["Social"])
        wholeActive = first
        wholeNot_active = second
        masterList = third
        return first and second and third

    # Active Persons
    @staticmethod
    def print_current_employees_in_list(whole_table):
        print("--------------------------------------------\n"
              "\tThese are the current Active persons sorted by SSN.\n"
              "--------------------------------------------\n"
              "==============")
        print("Row - Name - Address")
        counter = 0
        for row in whole_table:
            print(f'{counter + 1} | {row["Name"]} | {row["Address"]} | {row["Social"]} | {row["Date of Birth"]} |'
                  f'{row["Job Title"]} | {row["Start Date"]} | {row["End Date"]} |')
            counter += 1
        print("==============")

    # Inactive Persons
    @staticmethod
    def print_inactive_employees_in_list(whole_table):
        print("--------------------------------------------\n"
              "\tThese are the current Inactive persons sorted by SSN.\n"
              "--------------------------------------------\n"
              "==============")
        print("Row - Name - Address")
        counter = 0
        for row in whole_table:
            print(f'{counter + 1} | {row["Name"]} | {row["Address"]} | {row["Social"]} | {row["Date of Birth"]} |'
                  f'{row["Job Title"]} | {row["Start Date"]} | {row["End Date"]} |')
            counter += 1
        print("==============")

    @staticmethod
    def print_master_list(big_list):
        print("--------------------------------------------\n"
              "\tThese are all Persons on file sorted by SSN.\n"
              "--------------------------------------------\n"
              "==============")
        print("Row - Name - Address")
        counter = 0
        for row in big_list:
            print(f'{counter + 1} | {row["Name"]} | {row["Address"]} | {row["Social"]} | {row["Date of Birth"]} |'
                  f'{row["Job Title"]} | {row["Start Date"]} | {row["End Date"]} |')
            counter += 1
        print("==============")

    # Adds employee
    @staticmethod
    def add_employee_active():
        print("Please enter in the required information.")
        name = input("Employee Name: ")
        address = input("Employee Address: ")
        social = input("Social Security Number: ")
        dob = input("Date of Birth(MM/DD/YYYY): ")
        title = input("Job Title: ")
        start = input("Start Date (MM/DD/YYYY): ")
        end = input("Date Employee Left, if not applicable type -Active- (MM/DD/YYYY):")
        new_employee = [name, address, social, dob, title, start, end]
        with open("employees.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow(new_employee)
        print("{} has been added to the system.".format(name))

    @staticmethod
    def remove_employee_data():
        choice = input("Above is every single person in the system.\n"
                       "Which row associated with the employee do you want deleted?\n"
                       "Row Employee is on: ")
        yesno = input("!! Attention, This is permanent!!\n"
                      "Are you sure you want to delete this row?: ")
        yesno = yesno.lower().strip()
        if yesno == "yes":
            masterList.pop(int(choice) - 1)
            print("Row", choice, "has been removed permanently.")
        if yesno == "no":
            print("Row", choice, "has not been deleted.")
        else:
            print("Remove employee has been aborted.\n"
                  "Reason: Not Yes or No.")

    @staticmethod
    def save_data_to_csv_file(data_list):
        with open("employees.csv", mode="w") as csv_file:
            fieldnames = ["Name", "Address", "Social", "Date of Birth", "Job Title", "Start Date", "End Date"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            count = 0
            writer.writeheader()
            while count < len(data_list) - 1:
                writer.writerow(data_list[count])
                count += 1
            print("The file had been updated")


# Presentation


class Presentation:

    # Allows the user to choose options.
    @staticmethod
    def input_menu_choice():
        choice = str(input("Which option would you like to perform? [1 to 5] - "))
        print()
        return choice

    # Brings up the menu
    @staticmethod
    def print_menu_tasks():
        print("""
                   HR System
                *** Menu of Options ***
                1) Display Current Persons
                2) Display Inactive Persons
                3) Display All Persons
                4) Add Employee
                5) Remove Employee
                6) Save Data
                10) Exit
                
                *Reminder*:
                If needed data may be changed
                in the "employees.csv file       
                """)


# Main Script Body
Processor.read_data_from_file_master_list()
Processor.sort_data()
Processor.data_sorter_by_ssn(wholeActive, wholeNot_active, masterList)
while True:
    Presentation.print_menu_tasks()
    strChoice = Presentation.input_menu_choice()

    if strChoice.strip() == "1":
        Processor.print_current_employees_in_list(wholeActive)

    if strChoice.strip() == "2":
        Processor.print_inactive_employees_in_list(wholeNot_active)

    if strChoice.strip() == "3":
        Processor.print_master_list(masterList)

    if strChoice.strip() == "4":
        Processor.add_employee_active()
        Processor.update_file()
        Processor.sort_data()
        Processor.data_sorter_by_ssn(wholeActive, wholeNot_active, masterList)
        Processor.save_data_to_csv_file(masterList)

    if strChoice.strip() == "5":
        Processor.print_master_list(masterList)
        Processor.remove_employee_data()
        Processor.save_data_to_csv_file(masterList)
        Processor.sort_data()
        Processor.data_sorter_by_ssn(wholeActive, wholeNot_active, masterList)
        Processor.save_data_to_csv_file(masterList)

    if strChoice.strip() == "6":
        Processor.save_data_to_csv_file(masterList)

    if strChoice.strip() == "10":
        print("Goodbye!")
        break
