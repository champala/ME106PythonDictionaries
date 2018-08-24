import csv

'''
Author: Erick Garcia
Description: Python dictionaries and csv files
'''

'''
Part 1: The dictionary data type
'''
# person = {
# "EID":2907071, "Last Name": "Colvin", "First Name": "Claudette", "Address":"588 Example St.", "City": "Montgomery", "State": "AL", "Zip5": 36108, "Email 1": "claudette.colvin43@example.com", "Email 2": "","Phone 1": "3342423935", "Phone 2": "3345555934", "Volunteer": True, "Precinct Captain": True}

# 1. What are the ​keys​ in this dictionary?
# EID, Last Name, First Name, Address, City, State, Zip5, Email 1, Email 2, Phone 1, Phone 2, Volunteer, Precinct Captain.

# 2. What will the following return?
#     a. person["Address"]: 588 Example St.
#     b. person["Volunteer"]: True
#     c. person[Email 1]: syntax error
#     d. person["Phone 2"]: 3345555934
#     e. person['Phone 2']: 3345555934
#     f. person."Zip5": syntax error
#     g. person.Zip5: AttributeError
#     h. person[“Phone 1”][0:2]: syntaxError because of “, and 33 if fixed to "


'''
Part II: Using the CSV module
Part III: Writing CSVs module
Part IV: Adding Interactivity
'''

with open('volunteer.csv', 'r') as volunteer_file:
    totalPeople = 0  # Keeps count of all people (rows/records) on file
    volunteers = 0  # Keeps count of volunteers
    donors = 0  # Keeps count of donors
    csv_reader = csv.DictReader(volunteer_file)  # DictReader function to read volunteer.csv file
    for row in csv_reader:  # reads row by row
        # Counts volunteers and adds writes them to newVolunteerFile.csv with writenow function
        if row["Volunteer"] == "Yes":
            # Increments the volunteer counter
            volunteers += 1

        # Count Donors
        if row["Donor"] == "Yes":
            # Increments the donors counter
            donors += 1

        # Increments the total # of records read (total # of people on file).
        totalPeople += 1

    print("There are a total of " + str(totalPeople) + " people on this list. We have " + str(volunteers) + " volunteers and " + str(donors) + " donors.\n")

    # Ask user for csv file option
    userInput = input("Would you like a csv of: \n\t "
                      "1. All volunteers, or \n\t "
                      "2. Everyone on the list whose name starts with_? \n\t "
                      "Please reply with 1 or 2\n")

    # while loop to catch right csv option
    while userInput == "1" or "2":
        # Option 1 logic
        if userInput == "1":
            with open('volunteer.csv', 'r') as volunteer_file1:
                csv_reader = csv.DictReader(volunteer_file1)  # DictReader function to read volunteer.csv file
                with open('newVolunteerFile.csv', 'w') as newVolunteers_file: # Creates new document to write on
                    # sets header names for new file
                    headers = ["First Name", "Last Name", "City", "State", "Email 1", "Email 2", "Phone 1"]
                    # DictWriter function to specify where we are writing to, header line variable, and delimiter to use.
                    csv_writer = csv.DictWriter(newVolunteers_file, fieldnames=headers, delimiter=',')
                    csv_writer.writeheader()  # writes the column header line
                    for row in csv_reader:  # reads row by row
                        # Finds volunteers and adds them to newVolunteerFile.csv with writenow function
                        if row["Volunteer"] == "Yes":
                            csv_writer.writerow({"First Name": row["First Name"], "Last Name": row["Last Name"],
                                                 "City": row["City"], "State": row["State"], "Email 1": row["Email 1"],
                                                 "Email 2": row["Email 2"], "Phone 1": row["Phone 1"]})

                print("Volunteer csv file has been created!")
                exit()

        # Option 2 logic
        elif userInput == "2":
            firstNameInitial = input("Please enter a capital letter between A and Z: ")
            # while loop to look for alphabetic chars only (A-Z) and checks if it's upper case
            while firstNameInitial.isalpha() and firstNameInitial.isupper():
                # logic to read through doc
                with open('volunteer.csv', 'r') as volunteer_file1:
                    csv_reader = csv.DictReader(volunteer_file1)  # DictReader function to read volunteer.csv file
                    with open('fileThatStartswithLetter.csv', 'w') as newVolunteers_file:  # Creates new document to write on
                        # sets header names for new file
                        headers = ["First Name", "Last Name", "City", "State", "Email 1", "Email 2", "Phone 1"]
                        csv_writer = csv.DictWriter(newVolunteers_file, fieldnames=headers, delimiter=',')
                        csv_writer.writeheader()  # writes the column header line
                        for row in csv_reader: # reads row by row
                            # Checks for all First Name initial, compares to user letter and writes to new csv doc
                            if firstNameInitial == row["First Name"][0]:
                                csv_writer.writerow({"First Name": row["First Name"], "Last Name": row["Last Name"],
                                                 "City": row["City"], "State": row["State"], "Email 1": row["Email 1"],
                                                 "Email 2": row["Email 2"], "Phone 1": row["Phone 1"]})

                print("Your csv file with all names that start with " + firstNameInitial + " has been created!\n")
                exit()

        else:
            userInput = input("Please reply with 1 or 2.\n")