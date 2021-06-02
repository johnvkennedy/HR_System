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
ssn_data = ""
count = 0
checked_ssn = None


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
                          "Start Date": row["Start Date"], "End Date": row["End Date"], "Reviewed": row["Reviewed"]}
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
                          "Start Date": row["Start Date"], "End Date": row["End Date"], "Reviewed": row["Reviewed"]}
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
        print("\tThese are the current Active persons sorted by SSN.\n"
              "==========================================================")
        print("{:^18}".format("Row"), "{:^18}".format("Name"), "{:^18}".format("Address"), "{:^18}".format("SSN"),
              "{:^18}".format("Date of Birth"), "{:^18}".format("Job Title"), "{:^18}".format("Start Date"),
              "{:^18}".format("End Date/Active"), "{:^18}".format("Reviewed"))
        counter = 0
        for row in whole_table:
            print("{:^18}".format(counter + 1), "{:^18}".format(row["Name"]), "{:^18}".format(row["Address"]),
                  "{:^18}".format(row["Social"]), "{:^18}".format(row["Date of Birth"]),
                  "{:^18}".format(row["Job Title"]), "{:^18}".format(row["Start Date"]),
                  "{:^18}".format(row["End Date"]), "{:^18}".format(row["Reviewed"]))
            counter += 1

    # Inactive Persons
    @staticmethod
    def print_inactive_employees_in_list(whole_table):
        print("\tThese are the current Inactive persons sorted by SSN.\n"
              "============================================================")
        print("{:^18}".format("Row"), "{:^18}".format("Name"), "{:^18}".format("Address"), "{:^18}".format("SSN"),
              "{:^18}".format("Date of Birth"), "{:^18}".format("Job Title"), "{:^18}".format("Start Date"),
              "{:^18}".format("End Date/Active"), "{:^18}".format("Reviewed"))
        counter = 0
        for row in whole_table:
            print("{:^18}".format(counter + 1), "{:^18}".format(row["Name"]), "{:^18}".format(row["Address"]),
                  "{:^18}".format(row["Social"]), "{:^18}".format(row["Date of Birth"]),
                  "{:^18}".format(row["Job Title"]), "{:^18}".format(row["Start Date"]),
                  "{:^18}".format(row["End Date"]), "{:^18}".format(row["Reviewed"]))
            counter += 1

    @staticmethod
    def print_master_list(big_list):
        print("\tThese are all Persons on file sorted by SSN.\n"
              "===================================================")
        print("{:^18}".format("Row"), "{:^18}".format("Name"), "{:^18}".format("Address"), "{:^18}".format("SSN"),
              "{:^18}".format("Date of Birth"), "{:^18}".format("Job Title"), "{:^18}".format("Start Date"),
              "{:^18}".format("End Date/Active"), "{:^18}".format("Reviewed"))
        counter = 0
        for row in big_list:
            print("{:^18}".format(counter + 1), "{:^18}".format(row["Name"]), "{:^18}".format(row["Address"]),
                  "{:^18}".format(row["Social"]), "{:^18}".format(row["Date of Birth"]),
                  "{:^18}".format(row["Job Title"]), "{:^18}".format(row["Start Date"]),
                  "{:^18}".format(row["End Date"]), "{:^18}".format(row["Reviewed"]))
            counter += 1

    # Adds employee
    @staticmethod
    def add_employee_active():
        print("Please enter in the required information.")
        name = input("Employee Name: ")
        address = input("Employee Address: ")
        social = input("Social Security Number: ")
        dob = input("Date of Birth (YYYY-MM-DD)\n"
                    "EX: 1990-02-01: ")
        title = input("Job Title: ")
        start_year = input("Start Year (YYYY): ")
        start_month = input("Start Month (MM, NEEDS 0 AS PLACEHOLDER!): ")
        start_day = input("Start Day (DD, NEEDS 0 AS PLACEHOLDER!): ")
        end = input("Date Employee Left, if not applicable type -Active- (YYYY-MM-DD):")
        review = "Needs"
        print("Reviewed column is set to Needs by default.")
        new_employee = [name, address, social, dob, title,
                        "{}-{}-{}".format(start_year, start_month, start_day), end, review]
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
            fieldnames = ["Name", "Address", "Social", "Date of Birth",
                          "Job Title", "Start Date", "End Date", "Reviewed"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            count = 0
            writer.writeheader()
            while count < len(data_list) - 1:
                writer.writerow(data_list[count])
                count += 1
            print("The file had been updated")

    # Uses formatting to extract date from list
    @staticmethod
    def people_that_left_last_month(big_list):
        t_day = datetime.date.today()
        counter = 0
        print("Displaying persons who have left within a month\n"
              "NOTICE: If nothing shows up it could be no one\n"
              "         left within a month.\n")
        print("{:^18}".format("Row"), "{:^18}".format("Name"), "{:^18}".format("Address"), "{:^18}".format("SSN"),
              "{:^18}".format("Date of Birth"), "{:^18}".format("Job Title"), "{:^18}".format("Start Date"),
              "{:^18}".format("End Date/Active"), "{:^18}".format("Reviewed"))
        for i in big_list:
            try:
                test_date = str(big_list[counter].get("End Date")).replace("-", ",")
                year = int(test_date[0:4])
                month = ((test_date[5:7]).replace(" ", ""))
                month = int(month)
                day = ((test_date[8:11]).replace(" ", ""))
                day = int(day)
                total_date = datetime.date(year, month, day)
                dif = total_date - t_day
                dif = int(dif.days)
                if dif >= -30:
                    print("{:^18}".format(counter + 1), "{:^18}".format(i["Name"]), "{:^18}".format(i["Address"]),
                          "{:^18}".format(i["Social"]), "{:^18}".format(i["Date of Birth"]),
                          "{:^18}".format(i["Job Title"]), "{:^18}".format(i["Start Date"]),
                          "{:^18}".format(i["End Date"]), "{:^18}".format(i["Reviewed"]))
                counter += 1
            except ValueError:
                print("Value Error Occurred: Check the End Date column to see if\n"
                      "there is a date with no placeholder.\n"
                      "EX: 1990-01-01 = Works\n"
                      "EX: 1990-1-1 = Doesn't Work, Causes Error")

    @staticmethod
    def three_month_review(big_list):
        t_day = datetime.date.today()
        counter = 0
        print("Displaying persons who haven't had \n"
              "a review past 90 days from starting date.\n"
              "NOTICE: If nothing shows up it could be no one\n"
              "         needs a review.\n")
        print("{:^18}".format("Row"), "{:^18}".format("Name"), "{:^18}".format("Address"), "{:^18}".format("SSN"),
              "{:^18}".format("Date of Birth"), "{:^18}".format("Job Title"), "{:^18}".format("Start Date"),
              "{:^18}".format("End Date/Active"))
        for i in big_list:
            try:
                test_date = str(big_list[counter].get("Start Date")).replace("-", ",")
                year = int(test_date[0:4])
                month = ((test_date[5:7]).replace(" ", ""))
                month = int(month)
                day = ((test_date[8:11]).replace(" ", ""))
                day = int(day)
                total_date = datetime.date(year, month, day)
                dif = total_date - t_day
                dif = int(dif.days)
                if dif <= -90 and i["End Date"] == "Active" and i["Reviewed"] == "Needs":
                    print("{:^18}".format(counter + 1), "{:^18}".format(i["Name"]), "{:^18}".format(i["Address"]),
                          "{:^18}".format(i["Social"]), "{:^18}".format(i["Date of Birth"]),
                          "{:^18}".format(i["Job Title"]), "{:^18}".format(i["Start Date"]),
                          "{:^18}".format(i["End Date"]), "{:^18}".format(i["Reviewed"]))
                counter += 1
            except ValueError:
                print("Value Error Occurred: Check the Start Date column to see if\n"
                      "there is a date with no placeholder.\n"
                      "EX: 1990-01-01 = Works\n"
                      "EX: 1990-1-1 = Doesn't Work, Causes Error")

    @staticmethod
    def capture_ssn(ssn):
        try:
            global ssn_data
            ssn_data = str(input(ssn))
        except AttributeError:
            print("Please enter a SSN")

    @staticmethod
    def run_ssn_through_list(picked_ssn):
        global count
        while count < int(len(masterList) - 1):
            if picked_ssn.lower() == "back":
                print("You've Been Brought Back to Menu")
                count = 0
                break
            while picked_ssn != masterList[count].get('Social'):
                count += 1
                if count > len(masterList) - 1:
                    break
            try:
                print("You are accessing", masterList[count].get('Social'), masterList[count].get("Name"))
                global checked_ssn
                checked_ssn = picked_ssn
                break
            except IndexError:
                print("An error has occurred",
                      ssn_data, "is not a SSN in the data set")
                break

    @staticmethod
    def change_review():
        global count
        try:
            print(masterList[count].get("Name"), "has a review status of", masterList[count].get("Reviewed"),
                  "\nWould you like to change it to Finished if it's in the Needs status\n"
                  "or to the Needs status if it is currently Finished?")
            choice = input("Yes or No?: ")
            choice = choice.strip().lower()
            if choice == "yes":
                if masterList[count].get("Reviewed") == "Needs":
                    try:
                        masterList[count].update({"Reviewed": "Finished"})
                        count = 0
                        Processor.save_data_to_csv_file(masterList)
                    except AttributeError:
                        print("Error had occurred")
                        count = 0
                if masterList[count].get("Reviewed") == "Finished":
                    try:
                        masterList[count].update({"Reviewed": "Needs"})
                        count = 0
                        Processor.save_data_to_csv_file(masterList)
                    except AttributeError:
                        print("Error had occurred")
                        count = 0
            if choice == "no":
                count = 0
        except IndexError:
            count = 0

    @staticmethod
    def reset_ssn_data():
        global ssn_data
        ssn_data = ""


# Presentation


class Presentation:

    # Allows the user to choose options.
    @staticmethod
    def input_menu_choice():
        choice = str(input("Which option would you like to perform? [1 to 10] - "))
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
                7) Who has left with a month
                8) Who is in Need of a 3 Month Review
                9) Change Review Status
                10) Exit
                
                *Reminder*:
                If needed data may be changed
                in the "employees.csv file       
                """)

    @staticmethod
    def today_date():
        print("Today's Date Is:", datetime.date.today())

    @staticmethod
    def choose_ssn():
        print("Please enter the SSN of the person you'd\n"
              "like to change the status of.\n"
              "If it doesn't exist you'll be returned\n"
              "to the menu.\n"
              "EX: 111-11-1111\n"
              "It needs those lines in-between.")


# Main Script Body
Processor.read_data_from_file_master_list()
Processor.sort_data()
Processor.data_sorter_by_ssn(wholeActive, wholeNot_active, masterList)
Presentation.today_date()
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

    if strChoice.strip() == "7":
        Processor.people_that_left_last_month(wholeNot_active)

    if strChoice.strip() == "8":
        Processor.three_month_review(masterList)

    if strChoice.strip() == "9":
        Processor.print_master_list(masterList)
        Presentation.choose_ssn()
        Processor.capture_ssn(ssn_data)
        Processor.run_ssn_through_list(ssn_data)
        Processor.change_review()
        Processor.reset_ssn_data()

    if strChoice.strip() == "10":
        print("Goodbye!")
        break
