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

# Imports
import csv

# Data

dicRow = {}
# Primary data stored here
wholeActive = []
wholeNot_active = []
txtData = []


# Processing
class Processor:
    # Reads the CSV file and captures it into "wholeTable", a list that stores dictionaries
    @staticmethod
    def read_data_from_file():
        global dicRow
        with open('employees.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                dicRow = {"Name": row["name"], "Address": row["address"], "Social": row["ssn"],
                          "Date of Birth": row["date of birth"], "Job Title": row["job title"],
                          "Start Date": row["start date"], "End Date": row["end date"]}
                if dicRow["End Date"] == "Active":
                    wholeActive.append(dicRow)
                    line_count += 1
                else:
                    wholeNot_active.append(dicRow)
                    line_count += 1
            print(f'Processed {line_count} lines.')

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
    def print_current_employees_in_list(wholeTable):
        print("--------------------------------------------\n"
              "\tThese are the current Active persons.\n"
              "--------------------------------------------\n"
              "==============")
        print("Row - Name - Address")
        counter = 0
        for row in wholeTable:
            print(f'{counter + 1} | {row["Name"]} | {row["Address"]} | {row["Social"]} | {row["Date of Birth"]} |'
                  f'{row["Job Title"]} | {row["Start Date"]} | {row["End Date"]} |')
            counter += 1
        print("==============")

    # Inactive Persons
    @staticmethod
    def print_inactive_employees_in_list(wholeTable):
        print("--------------------------------------------\n"
              "\tThese are the current Inactive persons.\n"
              "--------------------------------------------\n"
              "==============")
        print("Row - Name - Address")
        counter = 0
        for row in wholeTable:
            print(f'{counter + 1} | {row["Name"]} | {row["Address"]} | {row["Social"]} | {row["Date of Birth"]} |'
                  f'{row["Job Title"]} | {row["Start Date"]} | {row["End Date"]} |')
            counter += 1
        print("==============")


# Presentation

# Main Script Body
Processor.read_data_from_file()
Processor.data_sorter(wholeActive, wholeNot_active)

Processor.print_current_employees_in_list(wholeActive)
Processor.print_inactive_employees_in_list(wholeNot_active)
print("\n")
print("FOR TESTING = Remove when finished")
print(wholeActive)
print(wholeNot_active)
