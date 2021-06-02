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
                dicRow = {"Name": row["name"], "Address": row["address"], "Social": row["ssn"],
                          "Date of Birth": row["date of birth"], "Job Title": row["job title"],
                          "Start Date": row["start date"], "End Date": row["end date"]}
                masterList.append(dicRow)
                line_count += 1

    @staticmethod
    def sort_data():
        line_count = 0
        for i in masterList:
            dicRow = masterList[i]
            if dicRow["End Date"] == "Active":
                wholeActive.append(dicRow)
                line_count += 1
            else:
                wholeNot_active.append(dicRow)
                line_count += 1

    @staticmethod
    def data_sorter(first, second):
        global wholeActive
        global wholeNot_active
        first = sorted(first, key=lambda i: i["Social"])
        second = sorted(second, key=lambda i: i["Social"])
        wholeActive = first
        wholeNot_active = second
        return first and second

    # Active Persons
    @staticmethod
    def print_current_employees_in_list(whole_table):
        print("--------------------------------------------\n"
              "\tThese are the current Active persons.\n"
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
              "\tThese are the current Inactive persons.\n"
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
              "\tThese are all Persons on file.\n"
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
        end = "Active"
        new_employee = [name, address, social, dob, title, start, end]
        with open("employees.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow(new_employee)
        print("{} has been added to the system.".format(name))
        masterList.append(new_employee)
        wholeActive.append(new_employee)

    @staticmethod
    def add_employee_inactive():
        print("Please enter in the required information.")
        name = input("Employee Name: ")
        address = input("Employee Address: ")
        social = input("Social Security Number: ")
        dob = input("Date of Birth(MM/DD/YYYY): ")
        title = input("Job Title: ")
        start = input("Start Date (MM/DD/YYYY): ")
        end = input("Date Employee Left: ")
        new_employee = [name, address, social, dob, title, start, end]
        with open("employees.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow(new_employee)
        print("{} has been added to the system.".format(name))
        wholeNot_active.append(new_employee)

    @staticmethod
    def remove_employee_data():
        pass


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
                5) Exit       
                """)


# Main Script Body
Processor.read_data_from_file_master_list()
Processor.sort_data()
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

    if strChoice.strip() == "5":
        Processor.add_employee_inactive()

    if strChoice.strip() == "10":
        print("Goodbye!")
        break
